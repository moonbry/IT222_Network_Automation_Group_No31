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
# SW1 VERIFICATION COMMANDS
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

    connection = ConnectHandler(**SW1)

    print("Connected to SW1")


    if SW1["secret"]:
        connection.enable()


    print("\n============================================")
    print(" SW1 VERIFICATION - Head Office")
    print("============================================")


    for command in verification_commands:

        print(f"\nCOMMAND: {command}")
        print("-" * 50)

        output = connection.send_command(command)

        print(output)


    print("\nSW1 verification completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"SW1 verification failed: {error}")