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
# R2 VERIFICATION COMMANDS
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

    connection = ConnectHandler(**R2)

    print("Connected to R2")


    if R2["secret"]:
        connection.enable()


    print("\n============================================")
    print(" R2 VERIFICATION - TRANSPORT TICKETING")
    print("============================================")


    for command in verification_commands:

        print(f"\nCOMMAND: {command}")
        print("-" * 50)

        output = connection.send_command(command)

        print(output)


    print("\nR2 verification completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"R2 verification failed: {error}")