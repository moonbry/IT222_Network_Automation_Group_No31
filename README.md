# IT 222 Network Automation – Assignment 31

## Head Office and Branch Integrated Network

---

# 1. Assignment Identification

| Item                | Details                                                   |
| ------------------- | --------------------------------------------------------- |
| Course              | IT 222                                                    |
| Assignment Number   | Assignment 31                                             |
| Scenario            | Head Office and Branch Integrated Network                 |
| Group Number        | Group 31                                                  |
| Technology          | Cisco IOS, VLAN, Router-on-a-Stick, OSPF, Python, Netmiko |
| Simulation Platform | GNS3                                                      |

---

# 2. Group Members

This project is completed by a group of four members.

| No. | Full Name             | Registration Number |
| --- | --------------------- | ------------------- | --------- |
| 1   | ALONI ASHELI KISIKI   | 2024/0440           |
| 2   | HARUNI HARUNI MADUMBA | 2023/0873           |
| 3   | AHMEDI MAJID IBRAHIM  |                     | 2024/1665 |
| 4   | MLYAPO H MLYAPO       | 2024/0475           |

---

# 3. Scenario Description

A company operates a Head Office and a Branch Office.

The company has two categories of users:

- Business users
- ITSupport personnel

Business users and ITSupport personnel must use separate VLANs at both
locations.

The routers provide:

- Inter-VLAN routing within each location
- Communication between the Head Office and Branch Office

The network is implemented and automated using Cisco IOS devices,
Python, and Netmiko.

The purpose of the project is not only to automate Cisco IOS commands,
but to demonstrate how a real-world networking requirement can be
translated into configuration, verification, testing, and an automated
engineering workflow.

---

# 4. Network Requirements

The network must satisfy the following requirements:

### Requirement 1 – User Separation

Business users and ITSupport users must be separated using different
VLANs at both the Head Office and Branch Office.

The VLANs used are:

- VLAN 59 – Business
- VLAN 89 – ITSupport

### Requirement 2 – Inter-VLAN Communication

Routers must provide inter-VLAN routing so that the Business and
ITSupport networks can communicate within each site.

### Requirement 3 – Inter-Site Communication

The Head Office and Branch Office must communicate through the
R1-to-R2 routed link.

### Requirement 4 – Dynamic Routing

OSPF process 1, area 0, is used to allow R1 and R2 to learn the
networks located at the opposite site.

### Requirement 5 – Network Automation

Python and Netmiko are used to automate:

- Device configuration
- Device verification
- Device testing
- Network-level verification
- Network-level testing

---

# 5. Topology Description

The network consists of two locations:

- Head Office / Site A
- Branch Office / Site B

The topology contains:

- R1
- R2
- SW1
- SW2
- Business-PC1
- IT-PC1
- Business-PC2
- IT-PC2

---

## 5.1 Head Office – Site A

R1 is the router for the Head Office.

SW1 connects the end devices to R1.

### SW1 Connections

```text
SW1 Gi0/1 -> R1 Gi0/0
SW1 Gi0/2 -> Business-PC1
SW1 Gi0/3 -> IT-PC1
Port Roles
Gi0/1 -> Trunk
Gi0/2 -> Access VLAN 59
Gi0/3 -> Access VLAN 89
5.2 Branch Office – Site B

R2 is the router for the Branch Office.

SW2 connects the end devices to R2.

SW2 Connections
SW2 Gi0/1 -> R2 Gi0/0
SW2 Gi0/2 -> Business-PC2
SW2 Gi0/3 -> IT-PC2
Port Roles
Gi0/1 -> Trunk
Gi0/2 -> Access VLAN 59
Gi0/3 -> Access VLAN 89
5.3 Router-to-Router Link

R1 and R2 are connected using:

R1 Gi0/1 ---------------- R2 Gi0/1
10.31.31.1/30             10.31.31.2/30

This link is used for communication between the two sites and OSPF
routing.

6. Network Addressing and VLANs
6.1 VLAN Information
VLAN ID	VLAN Name	Purpose
59	Business	Business users
89	ITSupport	ITSupport users
6.2 Head Office – Site A
Device	Interface	VLAN	IP Address
R1	Gi0/0.59	59	192.168.59.1/24
R1	Gi0/0.89	89	192.168.89.1/24
R1	Gi0/1	-	10.31.31.1/30
SW1	Gi0/1	Trunk	Allow 59,89
SW1	Gi0/2	59	Business-PC1
SW1	Gi0/3	89	IT-PC1
Business-PC1	NIC	59	192.168.59.10/24
IT-PC1	NIC	89	192.168.89.10/24
Head Office Gateways
Business VLAN:
Gateway = 192.168.59.1

ITSupport VLAN:
Gateway = 192.168.89.1
6.3 Branch Office – Site B
Device	Interface	VLAN	IP Address
R2	Gi0/0.59	59	192.168.159.1/24
R2	Gi0/0.89	89	192.168.189.1/24
R2	Gi0/1	-	10.31.31.2/30
SW2	Gi0/1	Trunk	Allow 59,89
SW2	Gi0/2	59	Business-PC2
SW2	Gi0/3	89	IT-PC2
Business-PC2	NIC	59	192.168.159.10/24
IT-PC2	NIC	89	192.168.189.10/24
Branch Office Gateways
Business VLAN:
Gateway = 192.168.159.1

ITSupport VLAN:
Gateway = 192.168.189.1
7. Routing Method
OSPF

The network uses:

OSPF Process: 1
Area: 0

OSPF is configured between R1 and R2 using the point-to-point network:

10.31.31.0/30
R1 OSPF Networks
192.168.59.0/24
192.168.89.0/24
10.31.31.0/30
R2 OSPF Networks
192.168.159.0/24
192.168.189.0/24
10.31.31.0/30

OSPF allows each router to learn the networks located at the opposite
site.

8. Scenario Requirements Analysis
Scenario Requirement	Configuration	Verification	Test
Business and ITSupport users must be separated	VLAN 59 for Business and VLAN 89 for ITSupport	show vlan brief, show interfaces switchport	Test Business and ITSupport connectivity
Inter-VLAN routing must be provided	R1/R2 router subinterfaces using 802.1Q	show ip interface brief, subinterface configuration	Business VLAN to local ITSupport VLAN
Head Office and Branch Office must communicate	R1-R2 routed link and OSPF	show ip ospf neighbor, show ip route ospf	Site A to Site B
Network configuration must be automated	Python and Netmiko scripts	Script output and device verification	Execute automated tests
9. Configuration Strategy

The configuration is divided into separate Python scripts for each
network device.

Each device follows the required engineering workflow:

Configure -> Verify -> Test
9.1 R1 Configuration

File:

Configuration_Scripts/r1_config.py

The R1 configuration script configures:

R1 hostname
Gi0/0 trunk-facing interface
VLAN 59 subinterface
VLAN 89 subinterface
R1-to-R2 interface
OSPF process 1
OSPF area 0
9.2 R1 Verification

File:

Configuration_Scripts/r1_verify.py

The R1 verification script checks:

Interface status
Router subinterfaces
VLAN 59 gateway
VLAN 89 gateway
OSPF neighbor
OSPF learned routes
Routing table

Important verification commands include:

show ip interface brief
show ip ospf neighbor
show ip route ospf
show ip route
9.3 R1 Testing

File:

Configuration_Scripts/r1_test.py

The R1 testing script performs tests related to R1's role in the
scenario.

The tests include:

R1 to R2 communication
Head Office Business VLAN to Branch Office Business VLAN
Head Office Business VLAN to local ITSupport VLAN
10. R2 Configuration Strategy
10.1 R2 Configuration

File:

Configuration_Scripts/r2_config.py

The R2 configuration script configures:

R2 hostname
Gi0/0 trunk-facing interface
VLAN 59 subinterface
VLAN 89 subinterface
R2-to-R1 interface
OSPF process 1
OSPF area 0
10.2 R2 Verification

File:

Configuration_Scripts/r2_verify.py

The R2 verification script checks:

Interface status
Router subinterfaces
OSPF neighbor
OSPF learned routes
Routing table

Important commands include:

show ip interface brief
show ip ospf neighbor
show ip route ospf
show ip route
10.3 R2 Testing

File:

Configuration_Scripts/r2_test.py

The R2 testing script performs tests related to the Branch Office.

The tests include:

R2 to R1 communication
Branch Office Business VLAN to Head Office Business VLAN
Branch Office Business VLAN to local ITSupport VLAN
11. SW1 Configuration Strategy
11.1 SW1 Configuration

File:

Configuration_Scripts/sw1_config.py

The SW1 configuration script configures:

VLAN 59 - Business
VLAN 89 - ITSupport

Port assignments:

Gi0/1 -> Trunk to R1
Gi0/2 -> Access VLAN 59 -> Business-PC1
Gi0/3 -> Access VLAN 89 -> IT-PC1
11.2 SW1 Verification

File:

Configuration_Scripts/sw1_verify.py

The SW1 verification script checks:

show vlan brief
show interfaces switchport
show interfaces trunk
show interfaces status

These checks confirm that VLANs, access ports, and trunks are correctly
configured.

11.3 SW1 Testing

File:

Configuration_Scripts/sw1_test.py

The SW1 test script verifies the switching-side behaviour required by
the scenario, including:

VLAN 59 assignment
VLAN 89 assignment
Correct access ports
Trunk operation
MAC address learning
12. SW2 Configuration Strategy
12.1 SW2 Configuration

File:

Configuration_Scripts/sw2_config.py

The SW2 configuration script configures:

VLAN 59 - Business
VLAN 89 - ITSupport

Port assignments:

Gi0/1 -> Trunk to R2
Gi0/2 -> Access VLAN 59 -> Business-PC2
Gi0/3 -> Access VLAN 89 -> IT-PC2
12.2 SW2 Verification

File:

Configuration_Scripts/sw2_verify.py

The SW2 verification script checks:

show vlan brief
show interfaces switchport
show interfaces trunk
show interfaces status
12.3 SW2 Testing

File:

Configuration_Scripts/sw2_test.py

The SW2 test script verifies the switching-side behaviour required by
the scenario, including:

VLAN 59 assignment
VLAN 89 assignment
Correct access ports
Trunk operation
MAC address learning
13. Network-Level Verification

After the four devices have individually completed:

Configure -> Verify -> Test

the integrated network is verified using:

network_verify.py

This script collects evidence from several devices.

It verifies:

VLANs
show vlan brief
Access Ports
show interfaces switchport
Trunks
show interfaces trunk
Router Subinterfaces
show ip interface brief
OSPF Neighbours
show ip ospf neighbor
Learned Routes
show ip route ospf

The purpose of the network-level verification is to demonstrate that
the complete topology is operating correctly.

14. Network-Level Testing

The integrated network is tested using:

network_test.py

The assignment requires the following tests.

Test 1 – Business-PC1 to Business-PC2
Source
Business-PC1
192.168.59.10
Destination
Business-PC2
192.168.159.10
Purpose

To verify that Business users can communicate between the Head Office
and Branch Office.

Expected Result

The destination should be reachable successfully.

Test 2 – IT-PC1 to IT-PC2
Source
IT-PC1
192.168.89.10
Destination
IT-PC2
192.168.189.10
Purpose

To verify that ITSupport users can communicate between the two sites.

Expected Result

The destination should be reachable successfully.

Test 3 – Business-PC1 to Local ITSupport VLAN
Source
Business-PC1
192.168.59.10
Destination
Local ITSupport VLAN
192.168.89.0/24
Purpose

To verify inter-VLAN routing at the Head Office.

Expected Result

The ITSupport destination should be reachable.

Test 4 – Business-PC2 to Local ITSupport VLAN
Source
Business-PC2
192.168.159.10
Destination
Local ITSupport VLAN
192.168.189.0/24
Purpose

To verify inter-VLAN routing at the Branch Office.

Expected Result

The ITSupport destination should be reachable.

Test 5 – R1 to R2
Source
R1
10.31.31.1
Destination
R2
10.31.31.2
Purpose

To verify the direct routed connection between the two routers.

Expected Result

R2 should respond successfully to R1.

Test 6 – Site A to Site B
Source
Site A / Head Office
Destination
Site B / Branch Office
Purpose

To verify complete inter-site communication.

Expected Result

Networks at Site A should communicate successfully with the
corresponding networks at Site B.

15. How to Run the Project
Step 1 – Open GNS3

Open the GNS3 project located in:

GNS3_Project_File/
Step 2 – Start All Devices

Start:

R1
R2
SW1
SW2
Business-PC1
IT-PC1
Business-PC2
IT-PC2

All required links should be operational before running the scripts.

Step 3 – Install Netmiko

Open a terminal in the project directory and run:

pip install netmiko
Step 4 – Configure TELNET Connection Values

The TELNET connection information is stored inside each Python script.

Example:

R1 = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.195.129",
    "username": "",
    "password": "",
    "secret": "",
    "port": 5012,
    "timeout": 500,
}

The host, port, username, password, and enable secret must match
the actual GNS3 device connection settings.

16. Script Execution Order

The assignment requires each device to follow:

Configure -> Verify -> Test

Therefore the recommended execution order is:

R1
python Configuration_Scripts/r1_config.py
python Configuration_Scripts/r1_verify.py
python Configuration_Scripts/r1_test.py
R2
python Configuration_Scripts/r2_config.py
python Configuration_Scripts/r2_verify.py
python Configuration_Scripts/r2_test.py
SW1
python Configuration_Scripts/sw1_config.py
python Configuration_Scripts/sw1_verify.py
python Configuration_Scripts/sw1_test.py
SW2
python Configuration_Scripts/sw2_config.py
python Configuration_Scripts/sw2_verify.py
python Configuration_Scripts/sw2_test.py
17. Integrated Network Verification

After all four devices have been configured, verified, and tested,
run:

python Configuration_Scripts/network_verify.py

This collects evidence from multiple devices and confirms that the
complete topology is operating correctly.

18. Integrated Network Testing

After network verification, run:

python Configuration_Scripts/network_test.py

This performs the scenario-based end-to-end tests:

Business-PC1 -> Business-PC2

IT-PC1 -> IT-PC2

Business-PC1 -> Local ITSupport VLAN

Business-PC2 -> Local ITSupport VLAN

R1 -> R2

Site A -> Site B
19. Expected Results

The completed network is expected to demonstrate:

VLANs
VLAN 59 -> Business
VLAN 89 -> ITSupport

Both VLANs should exist on SW1 and SW2.

Access Ports
SW1 Gi0/2 -> VLAN 59 -> Business-PC1
SW1 Gi0/3 -> VLAN 89 -> IT-PC1

SW2 Gi0/2 -> VLAN 59 -> Business-PC2
SW2 Gi0/3 -> VLAN 89 -> IT-PC2
Trunks
SW1 Gi0/1 -> R1 Gi0/0
Allowed VLANs: 59,89

SW2 Gi0/1 -> R2 Gi0/0
Allowed VLANs: 59,89
Router Subinterfaces
R1 Gi0/0.59 -> 192.168.59.1/24
R1 Gi0/0.89 -> 192.168.89.1/24

R2 Gi0/0.59 -> 192.168.159.1/24
R2 Gi0/0.89 -> 192.168.189.1/24
OSPF

R1 and R2 should form an OSPF neighbour relationship through:

10.31.31.0/30
Routing

R1 should learn the Branch Office networks:

192.168.159.0/24
192.168.189.0/24

R2 should learn the Head Office networks:

192.168.59.0/24
192.168.89.0/24
Connectivity

The required inter-VLAN and inter-site tests should succeed.

20. Project Folder Structure

The repository follows the required project structure.

IT222_Network_Automation_GroupXX/
│
├── Configuration_Scripts/
│   │
│   ├── r1_config.py
│   ├── r1_verify.py
│   ├── r1_test.py
│   │
│   ├── r2_config.py
│   ├── r2_verify.py
│   ├── r2_test.py
│   │
│   ├── sw1_config.py
│   ├── sw1_verify.py
│   ├── sw1_test.py
│   │
│   ├── sw2_config.py
│   ├── sw2_verify.py
│   ├── sw2_test.py
│   │
│   ├── network_verify.py
│   └── network_test.py
│
├── GNS3_Project_File/
│   └── [GNS3 project files]
│
├── Templates/
│   │
│   ├── network_test_template.py
│   ├── network_verify_template.py
│   ├── router_config_template.py
│   ├── router_test_template.py
│   ├── router_verify_template.py
│   ├── switch_config_template.py
│   ├── switch_test_template.py
│   └── switch_verify_template.py
│
├── Usage_Examples/
│   │
│   ├── network_test.py
│   ├── network_verify.py
│   ├── r1_config.py
│   ├── r1_test.py
│   ├── r1_verify.py
│   ├── sw1_config.py
│   ├── sw1_test.py
│   └── sw1_verify.py
│
└── README.md

The assignment specifically requires this organized repository structure,
including Configuration_Scripts, GNS3_Project_File, Templates,
Usage_Examples, and README.md.

21. Templates and Usage Examples

The original supplied templates are retained in:

Templates/

They are kept for reference and should not be treated as the completed
assignment scripts.

The supplied usage examples are retained in:

Usage_Examples/

The actual scenario-specific scripts are placed in:

Configuration_Scripts/

The assignment requires the supplied templates and usage examples to
remain available rather than simply renaming them as the final work.


22. Assumptions or Additional Features

No additional networking technology has been introduced beyond the
requirements of Assignment 31.

The implementation uses:

VLAN 59 for Business
VLAN 89 for ITSupport
802.1Q trunking
Router subinterfaces for inter-VLAN routing
OSPF process 1, area 0
Python
Netmiko

The IP addressing and device/interface assignments follow the network
data provided in Assignment 31.

23. GitHub Repository

The project is maintained in a GitHub repository.

Recommended repository name:

IT222_Network_Automation_GroupXX

The repository contains:

Configuration scripts
Verification scripts
Testing scripts
Network-level verification
Network-level testing
GNS3 project
Original templates
Usage examples
README documentation

The repository should be accessible to the lecturer for assessment.

24. Engineering Workflow

The complete project follows this workflow:

                ASSIGNMENT 31 REQUIREMENTS
                           |
                           v
                  NETWORK DESIGN
                           |
                           v
                  GNS3 TOPOLOGY
                           |
                           v
                  PYTHON CONFIGURATION
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
            R1            R2            SW1/SW2
             |             |             |
          Configure     Configure     Configure
             |             |             |
          Verify        Verify        Verify
             |             |             |
           Test          Test          Test
             +-------------+-------------+
                           |
                           v
                  NETWORK_VERIFY.PY
                           |
                           v
                   NETWORK_TEST.PY
                           |
                           v
                  TEST RESULTS/EVIDENCE

The purpose of this workflow is to demonstrate the relationship between
the scenario, network design, Python scripts, verification evidence,
test results, README documentation, and the GitHub repository.

25. Conclusion

Assignment 31 demonstrates the implementation and automation of a
Head Office and Branch Office integrated network.

Business users and ITSupport personnel are separated using VLAN 59 and
VLAN 89 at both locations.

Router subinterfaces provide inter-VLAN routing, while OSPF process 1,
area 0, provides dynamic routing between the Head Office and Branch
Office.

Python and Netmiko automate the configuration, verification, and
testing processes.

The final verification demonstrates VLANs, access ports, trunks,
router subinterfaces, OSPF neighbour formation, and learned routes.

The final network tests demonstrate the required communication between
Business users, ITSupport users, R1 and R2, and the two sites.

```
