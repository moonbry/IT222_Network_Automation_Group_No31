from netmiko import ConnectHandler


# ============================================
# R1 CONNECTION DETAILS
# ============================================

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group31",
    "port": 5012,
    "timeout": 500,
}


# ============================================
# R1 VERIFICATION COMMANDS
# ============================================

verification_commands = [

    "show ip interface brief",

    "show ip ospf neighbor",

    "show ip route",

    "show ip protocols",

    "show running-config | section router ospf",
]


# ============================================
# CONNECT AND VERIFY
# ============================================

try:

    connection = ConnectHandler(**R1)

    print("Connected to R1")


    if R1["secret"]:
        connection.enable()


    print("\n============================================")
    print(" R1 VERIFICATION - HEAD OFFICE")
    print("============================================")


    for command in verification_commands:

        print(f"\nCOMMAND: {command}")
        print("-" * 50)

        output = connection.send_command(command)

        print(output)


    print("\nR1 verification completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"R1 verification failed: {error}")