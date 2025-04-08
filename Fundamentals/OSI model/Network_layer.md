# Network Layer

## Overview
The **Network Layer** is the third layer in the OSI model, responsible for delivering packets from the source to the destination across multiple networks. It determines the best path for data transmission and handles logical addressing, routing, and packet forwarding.

## Responsibilities
1. **Logical Addressing**
   - Uses IP addresses to uniquely identify devices.
   - Provides hierarchical addressing for global communication.

2. **Routing**
   - Determines the best path for data packets.
   - Uses routing protocols like RIP, OSPF, and BGP.

3. **Packet Forwarding**
   - Transfers packets from one network to another.
   - Uses routers to direct traffic based on IP addresses.

4. **Fragmentation and Reassembly**
   - Splits large packets into smaller fragments for transmission.
   - Reassembles fragments at the destination.

## Key Protocols
- **Internet Protocol (IP)**: The primary protocol for addressing and routing packets.
- **Internet Control Message Protocol (ICMP)**: Used for diagnostic and error-reporting messages.
- **Address Resolution Protocol (ARP)**: Resolves IP addresses to MAC addresses.
- **Neighbor Discovery Protocol (NDP)**: Used in IPv6 for address resolution and router discovery.

## Network Layer Devices
- **Routers**: Direct packets between different networks.
- **Layer 3 Switches**: Perform routing functions within a network.

## Common Routing Algorithms
1. **Distance Vector Routing** (e.g., RIP)
   - Uses hop count as a metric.
   - Periodically updates routing tables.
   
2. **Link State Routing** (e.g., OSPF)
   - Uses a map of the network topology.
   - Floods network with link-state updates.
   
3. **Path Vector Routing** (e.g., BGP)
   - Used for inter-domain routing (between ISPs).
   - Maintains path information to avoid loops.

## Summary
The Network Layer is crucial for data delivery across networks, ensuring packets reach their intended destination efficiently. It relies on IP addressing, routing algorithms, and key protocols like IP, ICMP, and ARP to facilitate communication.
