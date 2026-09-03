from netmiko import ConnectHandler


# ============================================
# R2 CONNECTION DETAILS
# ============================================

R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5014,
    "timeout": 500,
}


# ============================================
# R2 CONFIGURATION
# Assignment 31 - Branch Office
#
# R2 Gi0/0 -> SW2 Gi0/1
# R2 Gi0/1 -> R1 Gi0/1
#
# VLAN 59 -> Business
# VLAN 89 -> ITSupport
# ============================================

configuration = [

    # ========================================
    # HOSTNAME
    # ========================================

    # Identify this router as R2.
    "hostname R2",


    # ========================================
    # PHYSICAL INTERFACE TO SW2
    # ========================================

    # Gi0/0 connects R2 to SW2.
    # The interface carries VLAN 59 and VLAN 89.
    "interface GigabitEthernet0/0",
    "description TRUNK_TO_SW2_Gi0/1",
    "no ip address",
    "no shutdown",


    # ========================================
    # VLAN 59 - BUSINESS
    # BRANCH OFFICE
    # ========================================

    # Business users at the Branch use:
    # Network: 192.168.159.0/24
    # Gateway: 192.168.159.1
    "interface GigabitEthernet0/0.59",
    "description BUSINESS_BRANCH",
    "encapsulation dot1Q 59",
    "ip address 192.168.159.1 255.255.255.0",
    "no shutdown",


    # ========================================
    # VLAN 89 - ITSUPPORT
    # BRANCH OFFICE
    # ========================================

    # ITSupport users at the Branch use:
    # Network: 192.168.189.0/24
    # Gateway: 192.168.189.1
    "interface GigabitEthernet0/0.89",
    "description ITSUPPORT_BRANCH",
    "encapsulation dot1Q 89",
    "ip address 192.168.189.1 255.255.255.0",
    "no shutdown",


    # ========================================
    # R2 TO R1 LINK
    # ========================================

    # Gi0/1 connects R2 to R1.
    #
    # R2 address: 10.31.31.2/30
    # R1 address: 10.31.31.1/30
    "interface GigabitEthernet0/1",
    "description R2_TO_R1_OSPF_LINK",
    "ip address 10.31.31.2 255.255.255.252",
    "no shutdown",


    # ========================================
    # OSPF CONFIGURATION
    # ========================================

    # Configure OSPF process 1.
    "router ospf 1",

    # Unique OSPF router ID for R2.
    "router-id 2.2.2.2",

    # Advertise Branch Business network.
    "network 192.168.159.0 0.0.0.255 area 0",

    # Advertise Branch ITSupport network.
    "network 192.168.189.0 0.0.0.255 area 0",

    # Advertise R1-R2 routed link.
    "network 10.31.31.0 0.0.0.3 area 0",


    # ========================================
    # SAVE CONFIGURATION
    # ========================================

    "do wr",
]


# ============================================
# CONNECT AND CONFIGURE R2
# ============================================

try:

    # Connect to R2 using Telnet.
    connection = ConnectHandler(**R2)

    print("Connected to R2")


    # Enter privileged EXEC mode.
    if R2["secret"]:
        connection.enable()


    # Send configuration commands.
    output = connection.send_config_set(configuration)


    print("\n===== R2 CONFIGURATION OUTPUT =====")
    print(output)


    # ========================================
    # VERIFICATION
    # ========================================

    # Verify R2 interfaces and subinterfaces.
    verification = connection.send_command(
        "show ip interface brief"
    )

    print("\n===== R2 INTERFACE VERIFICATION =====")
    print(verification)


    # Save running configuration.
    connection.save_config()

    print("\nR2 configuration saved successfully.")


    # Disconnect.
    connection.disconnect()


except Exception as error:

    print(f"R2 configuration failed: {error}")