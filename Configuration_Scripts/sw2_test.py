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
# SW2 TESTING COMMANDS
# ============================================

tests = {

    "TEST 1 - VERIFY Business VLAN 59":
    "show vlan id 59",

    "TEST 2 - VERIFY IT_Support VLAN 89":
    "show vlan id 89",

    "TEST 3 - VERIFY TRUNK TO R2":
    "show interfaces GigabitEthernet0/1 trunk",

    "TEST 4 - VERIFY Business PORT Gi0/2":
    "show interfaces GigabitEthernet0/2 switchport",

    "TEST 5 - VERIFY IT_Support PORT Gi0/3":
    "show interfaces GigabitEthernet0/3 switchport",
}


# ============================================
# CONNECT AND TEST
# ============================================

try:

    connection = ConnectHandler(**SW2)

    print("Connected to SW2")


    if SW2["secret"]:
        connection.enable()


    print("\n============================================")
    print(" SW2 TESTING - Branch Office")
    print("============================================")


    for test_name, command in tests.items():

        print(f"\n{test_name}")

        print(f"COMMAND: {command}")

        print("-" * 50)

        output = connection.send_command(command)

        print(output)


    print("\nSW2 testing completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"SW2 testing failed: {error}")