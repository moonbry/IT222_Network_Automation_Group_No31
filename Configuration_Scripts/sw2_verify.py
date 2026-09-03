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
# SW2 VERIFICATION COMMANDS
# ============================================

verification_commands = [

    "show vlan brief",

    "show vlan id 59",

    "show vlan id 89",

    "show interfaces trunk",

    "show interfaces status",
]


# ============================================
# CONNECT AND VERIFY
# ============================================

try:

    connection = ConnectHandler(**SW2)

    print("Connected to SW2")


    if SW2["secret"]:
        connection.enable()


    print("\n============================================")
    print(" SW2 VERIFICATION - Branch Office")
    print("============================================")


    for command in verification_commands:

        print(f"\nCOMMAND: {command}")
        print("-" * 50)

        output = connection.send_command(command)

        print(output)


    print("\nSW2 verification completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"SW2 verification failed: {error}")