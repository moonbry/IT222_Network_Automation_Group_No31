from netmiko import ConnectHandler


# ============================================
# SW2 CONNECTION DETAILS
# ============================================

SW2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group31",
    "port": 5018,
    "timeout": 500,
}


# ============================================
# SW2 CONFIGURATION
# Assignment 31 - Branch Office Switch
#
# Gi0/1 -> R2 Gi0/0
# Gi0/2 -> Business-PC2
# Gi0/3 -> IT-PC2
# ============================================

configuration = [

    # ========================================
    # HOSTNAME
    # ========================================

    # Identify this switch as SW2.
    "hostname SW2",


    # ========================================
    # VLAN 59 - BUSINESS
    # ========================================

    # VLAN 59 is used by Business users.
    "vlan 59",
    "name Business",


    # ========================================
    # VLAN 89 - ITSUPPORT
    # ========================================

    # VLAN 89 is used by ITSupport personnel.
    "vlan 89",
    "name ITSupport",


    # ========================================
    # TRUNK TO R2
    # ========================================

    # Gi0/1 connects SW2 to R2.
    #
    # The trunk carries:
    # VLAN 59 - Business
    # VLAN 89 - ITSupport
    "interface GigabitEthernet0/1",
    "description TRUNK_TO_R2_Gi0/0",
    "switchport mode trunk",
    "switchport trunk allowed vlan 59,89",
    "no shutdown",


    # ========================================
    # BUSINESS-PC2 PORT
    # ========================================

    # Gi0/2 connects Business-PC2.
    #
    # Business-PC2 belongs to VLAN 59.
    "interface GigabitEthernet0/2",
    "description BUSINESS_PC2",
    "switchport mode access",
    "switchport access vlan 59",
    "spanning-tree portfast",
    "no shutdown",


    # ========================================
    # IT-PC2 PORT
    # ========================================

    # Gi0/3 connects IT-PC2.
    #
    # IT-PC2 belongs to VLAN 89.
    "interface GigabitEthernet0/3",
    "description IT_PC2",
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
# CONNECT AND CONFIGURE SW2
# ============================================

try:

    # Connect to SW2.
    connection = ConnectHandler(**SW2)

    print("Connected to SW2")


    # Enter privileged EXEC mode.
    if SW2["secret"]:
        connection.enable()


    # Send configuration commands.
    output = connection.send_config_set(configuration)


    print("\n===== SW2 CONFIGURATION OUTPUT =====")
    print(output)


    # ========================================
    # VLAN VERIFICATION
    # ========================================

    # Verify VLAN 59 and VLAN 89.
    vlan_verification = connection.send_command(
        "show vlan brief"
    )

    print("\n===== SW2 VLAN VERIFICATION =====")
    print(vlan_verification)


    # ========================================
    # TRUNK VERIFICATION
    # ========================================

    # Verify that Gi0/1 carries VLAN 59 and 89.
    trunk_verification = connection.send_command(
        "show interfaces trunk"
    )

    print("\n===== SW2 TRUNK VERIFICATION =====")
    print(trunk_verification)


    # Save configuration.
    connection.save_config()

    print("\nSW2 configuration saved successfully.")


    # Disconnect.
    connection.disconnect()


except Exception as error:

    print(f"SW2 configuration failed: {error}")