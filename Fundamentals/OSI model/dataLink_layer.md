## Overview  
The **Data Link Layer** is the second layer of the OSI model. It provides reliable node-to-node data transfer and manages error detection, flow control, and media access control. This layer ensures that data frames are properly formatted and delivered across the physical network.  

# Key Responsibilities  

## 1. **Framing** 
   - what is framing : Framing is the process of encapsulating network-layer packets into data frames before transmission. The Data Link Layer uses framing to define boundaries for data and ensure error detection. Frames contain addressing information, synchronization data, and error-checking bits.

   - Encapsulates raw bits into structured **frames** for transmission.  
   - Adds headers and trailers containing control information.  
   ### Component of a frame

1- Header – Contains control information such as source and destination MAC

2- Payload (Data) – The actual data being transmitted (from the Network Layer).

3- Trailer – Contains error-checking information (e.g., CRC for error detection).

## 2. **Addressing (MAC and LLC)**  
### MAC (Media Access Control) addresses
- what is MAC addresse : A MAC address is a unique identifier assigned to a network interface card (NIC) of a device. It is used to distinguish devices on a local network (LAN).

**example for it**:
```
00:1A:2B:3C:4D:5E
```
### example for MAC addresse
|Type|Description|
|----|-----------|
|Unicast|Frame is sent to a specific device (one-to-one communication).|
|Multicast|Frame is sent to multiple devices in a group (one-to-many).|
|Broadcast|Frame is sent to all devices in the network (one-to-all) ```Example: FF:FF:FF:FF:FF:FF```|

### How MAC Addressing Works
- When a device sends a frame, it includes:
  - Source MAC Address (Sender’s NIC address).
  - Destination MAC Address (Receiver’s NIC address).
- Switches use MAC address tables to forward frames to the correct device.
**Example: Ethernet Frame MAC Addressing**
```
| Destination MAC | Source MAC | Data | CRC |
```

   ### LLC (Logical Link Control)  
The **LLC sublayer** provides a way to identify network layer protocols inside a frame.

### LLC Functions
 - Multiplexing: Allows multiple network protocols (IPv4, IPv6, ARP) to use the same physical network. 

 - Flow control: Prevents data overflow or loss.

 - Error detection: Identifies transmission errors.

## 3. **Error Detection and Correction**  
   - Uses techniques like **Cyclic Redundancy Check (CRC)** to detect errors in frames.  
   - Some protocols implement error correction (e.g., Automatic Repeat reQuest - ARQ).  

## 4. **Flow Control**  
   - Prevents a fast sender from overwhelming a slow receiver.  
   - Methods include **stop-and-wait** and **sliding window** protocols.  

## 5. **Media Access Control (MAC)**  
   - Controls how devices share the transmission medium.  
   - Two main types of MAC methods:  
     - **Contention-based (CSMA/CD, CSMA/CA)** – Devices compete for access.  
     - **Token-based (Token Ring, FDDI)** – Devices transmit only when they have a token.  

## 6. **Link Establishment and Termination**  
   - Handles the initiation and closing of communication between directly connected devices.  

## Sublayers of the Data Link Layer  

The Data Link Layer is divided into two sublayers:  

1. **Logical Link Control (LLC) Sublayer**  
   - Provides error detection, flow control, and interface to the Network Layer.  
   - Works independently of the physical medium.  

2. **Media Access Control (MAC) Sublayer**  
   - Manages access to the physical medium.  
   - Defines unique MAC addresses for devices.  
   - Implements protocols like Ethernet, Wi-Fi, and Bluetooth.  

## Common Data Link Layer Protocols  

| Protocol | Description |  
|----------|------------|  
| Ethernet (IEEE 802.3) | Wired LAN protocol using CSMA/CD for access control. |  
| Wi-Fi (IEEE 802.11) | Wireless LAN protocol using CSMA/CA. |  
| PPP (Point-to-Point Protocol) | Used in direct communication links (e.g., dial-up, DSL). |  
| HDLC (High-Level Data Link Control) | Used in point-to-point and multipoint communication. |  
| Token Ring (IEEE 802.5) | Uses a token-passing mechanism for network access. |  

## Error Detection Techniques  

- **Parity Bit** – Adds a single bit to detect errors in small data blocks.  
- **Checksum** – Calculates a sum of transmitted data for integrity verification.  
- **Cyclic Redundancy Check (CRC)** – Generates a mathematical checksum to detect errors in large frames.  

## How the Data Link Layer Works  

1. A **sending device** encapsulates network-layer packets into **frames**.  
2. The frame is **addressed** using MAC addresses.  
3. The frame is transmitted via the **Physical Layer**.  
4. The **receiving device** extracts the frame and verifies it using error detection techniques.  
5. If no errors are found, the frame's payload is passed to the **Network Layer**.  

## Summary  

- The Data Link Layer ensures reliable transmission over physical networks.  
- It uses **framing, MAC addressing, error detection, and flow control** to manage data transfer.  
- Divided into **LLC** (error control) and **MAC** (media access control) sublayers.  
- Protocols like **Ethernet, Wi-Fi, and PPP** operate at this layer.  

