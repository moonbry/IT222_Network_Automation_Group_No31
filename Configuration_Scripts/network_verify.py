from netmiko import ConnectHandler


devices = {
    "R1": {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5012,
    },

    "R2": {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5014,
    },

    "SW1": {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group31",
    "port": 5016,
    "timeout" : 500,
    },

    "SW2": {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "group31",
    "port": 5018,
    "timeout" : 500,
    },
}


verification_commands = {

    "R1": [
        "show ip interface brief",
        "show ip ospf neighbor",
        "show ip route ospf",
    ],

    "R2": [
        "show ip interface brief",
        "show ip ospf neighbor",
        "show ip route ospf",
    ],

    "SW1": [
        "show vlan brief",
        "show interfaces trunk",
    ],

    "SW2": [
        "show vlan brief",
        "show interfaces trunk",
    ],
}


for device_name, device in devices.items():

    print("\n")
    print("=" * 60)
    print(f"VERIFYING {device_name}")
    print("=" * 60)

    try:
        connection = ConnectHandler(**device)

        for command in verification_commands[device_name]:

            print(f"\n----- {command} -----")

            output = connection.send_command(command)

            print(output)

        connection.disconnect()

    except Exception as error:
        print(f"{device_name} verification failed: {error}")