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
# R2 TESTING COMMANDS
# ============================================

tests = {

    "TEST 1 - R2 TO R1 WAN CONNECTIVITY":
    "ping 10.31.31.1",

    "TEST 2 - Branch TO Head Office TICKETING NETWORK":
    "ping 192.168.59.1",

    "TEST 3 - Branch TO Head Office OPERATIONS NETWORK":
    "ping 192.168.89.1",

        ##Test if you already set ip on firefox docker for success ping

    "TEST 4 - Branch Business TERMINAL":
    "ping 192.168.159.10",

    "TEST 5 - Branch OPERATIONS COMPUTER":
    "ping 192.168.189.10",
}


# ============================================
# CONNECT AND TEST
# ============================================

try:

    connection = ConnectHandler(**R2)

    print("Connected to R2")


    if R2["secret"]:
        connection.enable()


    print("\n============================================")
    print(" R2 TESTING - TRANSPORT TICKETING NETWORK")
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


    print("\nR2 testing completed successfully.")

    connection.disconnect()


except Exception as error:

    print(f"R2 testing failed: {error}")