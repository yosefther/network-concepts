# Subnetting IPv4

## Overview
Subnetting in IPv4 is the process of dividing a large network into smaller, more manageable sub-networks, known as subnets. This allows more efficient use of IP address space, improves network performance, and enhances security. Subnetting is crucial in IPv4 networks because of the limited availability of IP addresses.

## Key Concepts
1. **IP Address**: An IPv4 address is a 32-bit number typically written as four octets (bytes), separated by periods (e.g., `192.168.1.1`).
2. **Subnet Mask**: A subnet mask is used to divide an IP address into network and host parts. It is also a 32-bit address and helps identify which portion of the IP address refers to the network and which part refers to the host.
3. **Network Address**: The first address of a subnet, used to identify the subnet itself.
4. **Broadcast Address**: The last address in a subnet, used to send data to all devices within the subnet.
5. **Host Address**: The address assigned to devices within a subnet.

## IPv4 Address Classes
IPv4 addresses are categorized into different classes based on their size and usage. These are the main classes:
- **Class A**: `0.0.0.0 - 127.255.255.255` (supports 16 million hosts per network)
- **Class B**: `128.0.0.0 - 191.255.255.255` (supports 65,000 hosts per network)
- **Class C**: `192.0.0.0 - 223.255.255.255` (supports 254 hosts per network)
- **Class D (Multicast)**: `224.0.0.0 - 239.255.255.255`
- **Class E (Reserved)**: `240.0.0.0 - 255.255.255.255`

## Subnetting Process

### Step 1: Identify the Network Address and Subnet Mask
- Start with a given IP address and its default subnet mask. For example, for a **Class C** address `192.168.1.0/24`, the subnet mask is `255.255.255.0`.

### Step 2: Borrow Bits from the Host Portion
To create subnets, we "borrow" bits from the host portion of the IP address. The number of bits borrowed determines how many subnets you can create and how many hosts can be in each subnet.

- **Class C Default Subnet Mask**: `/24` (255.255.255.0), with 8 bits for hosts.
- If you borrow 2 bits from the host portion, you create 4 subnets (2^2 = 4), and the new subnet mask becomes `/26` (255.255.255.192).

### Step 3: Calculate the Number of Subnets and Hosts
The number of subnets and hosts depends on how many bits you borrow from the host part:
- **Number of Subnets** = 2^n, where `n` is the number of bits borrowed.
- **Number of Hosts per Subnet** = 2^h - 2, where `h` is the number of remaining bits in the host portion. We subtract 2 for the network and broadcast addresses.

### Step 4: Assign IP Address Ranges to Subnets
Each subnet will have its own network address, broadcast address, and a range of usable IP addresses.

### Example: Subnetting a Class C Network

Given: `192.168.1.0/24` and we need 4 subnets.

1. **Step 1: Subnet Mask**
   - Borrow 2 bits from the host portion (8 bits).
   - New subnet mask: `/26` (255.255.255.192).

2. **Step 2: Calculate Subnets**
   - Number of subnets: 2^2 = 4.
   - Number of hosts per subnet: 2^6 - 2 = 62 usable hosts.

3. **Step 3: Assign IP Ranges**
   - **Subnet 1**: 192.168.1.0/26 (Network: 192.168.1.0, Broadcast: 192.168.1.63, Usable IPs: 192.168.1.1 - 192.168.1.62)
   - **Subnet 2**: 192.168.1.64/26 (Network: 192.168.1.64, Broadcast: 192.168.1.127, Usable IPs: 192.168.1.65 - 192.168.1.126)
   - **Subnet 3**: 192.168.1.128/26 (Network: 192.168.1.128, Broadcast: 192.168.1.191, Usable IPs: 192.168.1.129 - 192.168.1.190)
   - **Subnet 4**: 192.168.1.192/26 (Network: 192.168.1.192, Broadcast: 192.168.1.255, Usable IPs: 192.168.1.193 - 192.168.1.254)

## Subnetting Table for Class C (Example)

| Subnet | Network Address | First Usable IP | Last Usable IP | Broadcast Address | Subnet Mask |
|--------|-----------------|-----------------|----------------|-------------------|-------------|
| 1      | 192.168.1.0     | 192.168.1.1     | 192.168.1.62   | 192.168.1.63      | 255.255.255.192 |
| 2      | 192.168.1.64    | 192.168.1.65    | 192.168.1.126  | 192.168.1.127     | 255.255.255.192 |
| 3      | 192.168.1.128   | 192.168.1.129   | 192.168.1.190  | 192.168.1.191     | 255.255.255.192 |
| 4      | 192.168.1.192   | 192.168.1.193   | 192.168.1.254  | 192.168.1.255     | 255.255.255.192 |

## CIDR (Classless Inter-Domain Routing)
CIDR notation is a more flexible method of specifying network addresses. Instead of using a subnet mask, CIDR uses a slash (`/`) followed by the number of bits in the network portion. For example, `192.168.1.0/24` specifies a network with a 24-bit network portion.

### Example of CIDR Subnetting:
- **192.168.1.0/24** means a network with a subnet mask of `255.255.255.0`.
- **192.168.1.0/26** means a network with a subnet mask of `255.255.255.192`.

## Conclusion
Subnetting IPv4 is an essential skill for network administrators and engineers. It helps optimize the usage of IP address space, ensures better network management, and improves overall performance and security. Understanding how to calculate subnets, hosts, and subnet masks is crucial for designing efficient and scalable networks.
