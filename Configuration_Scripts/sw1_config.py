from netmiko import ConnectHandler


# ============================================
# SW1 CONNECTION DETAILS
# ============================================

SW1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group31",
    "port": 5016,
    "timeout": 500,
}


# ============================================
# SW1 CONFIGURATION
# Assignment 31 - Head Office Switch
#
# Gi0/1 -> R1 Gi0/0
# Gi0/2 -> Business-PC1
# Gi0/3 -> IT-PC1
# ============================================

configuration = [

    # ========================================
    # HOSTNAME
    # ========================================

    # Identify this switch as SW1.
    "hostname SW1",


    # ========================================
    # VLAN 59 - BUSINESS
    # ========================================

    # VLAN 59 separates Business users
    # from ITSupport users.
    "vlan 59",
    "name Business",


    # ========================================
    # VLAN 89 - ITSUPPORT
    # ========================================

    # VLAN 89 provides a separate network
    # for ITSupport personnel.
    "vlan 89",
    "name ITSupport",


    # ========================================
    # TRUNK TO R1
    # ========================================

    # Gi0/1 connects SW1 to R1.
    #
    # The trunk carries:
    # VLAN 59 - Business
    # VLAN 89 - ITSupport
    "interface GigabitEthernet0/1",
    "description TRUNK_TO_R1_Gi0/0",
    "switchport mode trunk",
    "switchport trunk allowed vlan 59,89",
    "no shutdown",


    # ========================================
    # BUSINESS-PC1 PORT
    # ========================================

    # Gi0/2 connects Business-PC1.
    #
    # Business-PC1 belongs to VLAN 59.
    "interface GigabitEthernet0/2",
    "description BUSINESS_PC1",
    "switchport mode access",
    "switchport access vlan 59",
    "spanning-tree portfast",
    "no shutdown",


    # ========================================
    # IT-PC1 PORT
    # ========================================

    # Gi0/3 connects IT-PC1.
    #
    # IT-PC1 belongs to VLAN 89.
    "interface GigabitEthernet0/3",
    "description IT_PC1",
    "switchport mode access",
    "switchport access vlan 89",
    "spanning-tree portfast",
    "no shutdown",


    # ========================================
    # SAVE CONFIGURATION
    # ========================================

    "do wr",
]


# ============================================
# CONNECT AND CONFIGURE SW1
# ============================================

try:

    # Connect to SW1.
    connection = ConnectHandler(**SW1)

    print("Connected to SW1")


    # Enter privileged EXEC mode.
    if SW1["secret"]:
        connection.enable()


    # Send configuration to SW1.
    output = connection.send_config_set(configuration)


    print("\n===== SW1 CONFIGURATION OUTPUT =====")
    print(output)


    # ========================================
    # VLAN VERIFICATION
    # ========================================

    # Verify VLAN 59 and VLAN 89 exist.
    vlan_verification = connection.send_command(
        "show vlan brief"
    )

    print("\n===== SW1 VLAN VERIFICATION =====")
    print(vlan_verification)


    # ========================================
    # TRUNK VERIFICATION
    # ========================================

    # Verify Gi0/1 is carrying VLAN 59 and VLAN 89.
    trunk_verification = connection.send_command(
        "show interfaces trunk"
    )

    print("\n===== SW1 TRUNK VERIFICATION =====")
    print(trunk_verification)


    # Save configuration.
    connection.save_config()

    print("\nSW1 configuration saved successfully.")


    # Disconnect.
    connection.disconnect()


except Exception as error:

    print(f"SW1 configuration failed: {error}")