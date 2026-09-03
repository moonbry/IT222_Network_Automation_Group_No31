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
# R1 TESTING COMMANDS
# ============================================

tests = {

    "TEST 1 - R1 TO R2 WAN CONNECTIVITY":
    "ping 10.31.31.2",

    "TEST 2 - Head Office TO Branch Business NETWORK":
    "ping 192.168.159.1",

    "TEST 3 - Head Office TO Branch IT_Support NETWORK":
    "ping 192.168.189.1",

    ##Test if you already set ip on firefox docker for success ping

    "TEST 4 - Head Office Busiiness TERMINAL":
    "ping 192.168.59.10",

    "TEST 5 - Head Office IT_Support COMPUTER":
    "ping 192.168.89.10",
}


# ============================================
# CONNECT AND TEST
# ============================================

try:

    connection = ConnectHandler(**R1)

    print("Connected to R1")


    if R1["secret"]:
        connection.enable()


    print("\n============================================")
    print(" R1 TESTING - TRANSPORT TICKETING NETWORK")
    print("============================================")


    for test_name, command in tests.items():

        print(f"\n{test_name}")

        print(f"COMMAND: {command}")

        print("-" * 50)

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)


    print("\nR1 testing completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"R1 testing failed: {error}")