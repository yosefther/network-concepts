# **TCP Packet Types**

## **1. SYN (Synchronize)**
A `SYN` message is the initial packet sent by a client during the TCP handshake. This packet is used to initiate a connection and synchronize the sequence numbers between the two devices. It essentially signals the intent to establish a connection.

- **Purpose:** Initiates a connection request.
- **Key Data:** Sequence number (SEQ) chosen by the client.
- **Example:** `Client → Server: [SYN, SEQ = x]`

## **2. SYN/ACK (Synchronize-Acknowledge)**
Once the server receives the `SYN` packet, it responds with a `SYN/ACK` message. This acknowledges the client's request while also initiating its own synchronization request.

- **Purpose:** Acknowledges the `SYN` and establishes synchronization.
- **Key Data:** Server's sequence number and ACK for the client's `SYN`.
- **Example:** `Server → Client: [SYN, ACK, SEQ = y, ACK = x + 1]`

## **3. ACK (Acknowledge)**
The `ACK` packet is sent by either the client or server to confirm successful reception of previous packets. It plays a crucial role in ensuring reliable communication.

- **Purpose:** Confirms receipt of previous packets.
- **Key Data:** Acknowledgment number (ACK) indicating the next expected sequence number.
- **Example:** `Client → Server: [ACK, SEQ = x + 1, ACK = y + 1]`

## **4. DATA (Payload Transmission)**
Once a connection has been established, data transmission begins. The `DATA` packets contain the actual information being exchanged, such as text, images, or files.

- **Purpose:** Transfers actual data between devices.
- **Key Data:** Sequence number to maintain order and integrity of data.
- **Example:** `Client → Server: [DATA, SEQ = x + 1, ACK = y + 1]`

## **5. FIN (Finish)**
A `FIN` packet is used to initiate a graceful termination of the connection. When a device has finished transmitting data, it sends a `FIN` message to indicate it will no longer send further packets.

- **Purpose:** Closes a connection in an orderly fashion.
- **Key Data:** Sequence number marking the end of transmission.
- **Example:** `Client → Server: [FIN, SEQ = x + n]`

## **6. RST (Reset - Connection Termination)**
An `RST` packet is sent when an abrupt termination is required. This happens if an error occurs, such as an unavailable service, an application crash, or resource exhaustion. Unlike `FIN`, the `RST` message immediately ends the session without waiting for an acknowledgment.

- **Purpose:** Terminates a connection immediately due to an error.
- **Key Data:** No formal sequence number negotiation.
- **Example:** `Server → Client: [RST]`

