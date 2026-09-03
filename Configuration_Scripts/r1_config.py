from netmiko import ConnectHandler


# ============================================
# R1 CONNECTION DETAILS
# ============================================

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5012,
    "timeout": 500,
}


# ============================================
# R1 CONFIGURATION
# Assignment 31 - Head Office and Branch
#
# R1 Gi0/0 -> SW1 Gi0/1
# R1 Gi0/1 -> R2 Gi0/1
#
# VLAN 59 -> Business
# VLAN 89 -> ITSupport
# ============================================

configuration = [

    # ========================================
    # HOSTNAME
    # ========================================

    # Identify this router as R1
    "hostname R1",


    # ========================================
    # PHYSICAL INTERFACE TO SW1
    # ========================================

    # Gi0/0 connects R1 to SW1.
    # This interface carries VLAN 59 and VLAN 89
    # using an 802.1Q trunk.
    "interface GigabitEthernet0/0",
    "description TRUNK_TO_SW1_Gi0/1",
    "no ip address",
    "no shutdown",


    # ========================================
    # VLAN 59 - BUSINESS
    # HEAD OFFICE
    # ========================================

    # Create the router subinterface for
    # Business users at Head Office.
    #
    # Network: 192.168.59.0/24
    # Gateway: 192.168.59.1
    "interface GigabitEthernet0/0.59",
    "description BUSINESS_HEAD_OFFICE",
    "encapsulation dot1Q 59",
    "ip address 192.168.59.1 255.255.255.0",
    "no shutdown",


    # ========================================
    # VLAN 89 - ITSUPPORT
    # HEAD OFFICE
    # ========================================

    # Create the router subinterface for
    # ITSupport users at Head Office.
    #
    # Network: 192.168.89.0/24
    # Gateway: 192.168.89.1
    "interface GigabitEthernet0/0.89",
    "description ITSUPPORT_HEAD_OFFICE",
    "encapsulation dot1Q 89",
    "ip address 192.168.89.1 255.255.255.0",
    "no shutdown",


    # ========================================
    # R1 TO R2 LINK
    # ========================================

    # Gi0/1 connects R1 to R2.
    #
    # R1 address: 10.31.31.1/30
    # R2 address: 10.31.31.2/30
    #
    # This link provides communication between
    # Head Office and Branch Office.
    "interface GigabitEthernet0/1",
    "description R1_TO_R2_OSPF_LINK",
    "ip address 10.31.31.1 255.255.255.252",
    "no shutdown",


    # ========================================
    # OSPF CONFIGURATION
    # ========================================

    # OSPF process 1 is required by Assignment 31.
    "router ospf 1",

    # Router ID uniquely identifies R1 in OSPF.
    "router-id 1.1.1.1",

    # Advertise Head Office Business network.
    "network 192.168.59.0 0.0.0.255 area 0",

    # Advertise Head Office ITSupport network.
    "network 192.168.89.0 0.0.0.255 area 0",

    # Advertise R1-R2 routed link.
    "network 10.31.31.0 0.0.0.3 area 0",


    # ========================================
    # SAVE CONFIGURATION
    # ========================================

    "do wr",
]


# ============================================
# CONNECT AND CONFIGURE R1
# ============================================

try:

    # Establish Telnet connection to R1.
    connection = ConnectHandler(**R1)

    print("Connected to R1")


    # Enter privileged EXEC mode if
    # an enable secret is configured.
    if R1["secret"]:
        connection.enable()


    # Send all configuration commands to R1.
    output = connection.send_config_set(configuration)


    # Display configuration output.
    print("\n===== R1 CONFIGURATION OUTPUT =====")
    print(output)


    # ========================================
    # VERIFICATION
    # ========================================

    # Verify physical interfaces and
    # router subinterfaces.
    verification = connection.send_command(
        "show ip interface brief"
    )

    print("\n===== R1 INTERFACE VERIFICATION =====")
    print(verification)


    # ========================================
    # SAVE CONFIGURATION
    # ========================================

    connection.save_config()

    print("\nR1 configuration saved successfully.")


    # Disconnect from R1.
    connection.disconnect()


except Exception as error:

    print(f"R1 configuration failed: {error}")