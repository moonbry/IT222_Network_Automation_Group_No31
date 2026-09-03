from netmiko import ConnectHandler


# =========================================================
# ROUTER CONNECTIONS
# =========================================================

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5012,
}

R2 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5014,
}


# =========================================================
# NETWORK TESTS
# =========================================================

r1_tests = {

    "R1 to R2": "ping 10.31.31.2",

    "HeadOffice Business-PC-1 gateway to Branch Business-PC-2 gateway":
        "ping 192.168.159.1",

    "HeadOffice IT_Support-PC-1 gateway to Branch IT_Support-PC-2 gateway":
        "ping 192.168.189.1",

}


r2_tests = {

    "R2 to R1": "ping 10.31.31.1",

    "Branch Business-PC-2 gateway to HeadOffice Business-PC-1 gateway":
        "ping 172.28.59.1",

    "Branch IT_Support-PC-2 gateway to HeadOffice IT_Support-PC-1 gateway":
        "ping 172.28.89.1",

}


# =========================================================
# TEST R1
# =========================================================

print("\n" + "=" * 60)
print("SITE A / R1 TESTING")
print("=" * 60)

try:

    connection = ConnectHandler(**R1)

    for purpose, command in r1_tests.items():

        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)

        print(output)

    connection.disconnect()

except Exception as error:

    print(f"R1 testing failed: {error}")


# =========================================================
# TEST R2
# =========================================================

print("\n" + "=" * 60)
print("SITE B / R2 TESTING")
print("=" * 60)

try:

    connection = ConnectHandler(**R2)

    for purpose, command in r2_tests.items():

        print(f"\nTEST: {purpose}")
        print(f"COMMAND: {command}")

        output = connection.send_command(command)

        print(output)

    connection.disconnect()

except Exception as error:

    print(f"R2 testing failed: {error}")