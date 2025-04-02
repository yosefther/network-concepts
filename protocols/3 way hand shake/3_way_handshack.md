# **TCP 3-Way Handshake**

The **TCP 3-way handshake** is the fundamental process used to establish a reliable connection between a client and a server before data transmission begins. This mechanism ensures that both parties are synchronized and ready to communicate.

## **Step 1: SYN (Synchronize)**
The client initiates the connection by sending a `SYN` (synchronize) packet to the server. This packet contains an initial **sequence number** that will be used for the communication session.

- Purpose: Initiates the connection and synchronizes sequence numbers.
- Example:
  ```
  Client → Server: [SYN, SEQ = x]
  ```

## **Step 2: SYN/ACK (Synchronize-Acknowledge)**
Upon receiving the `SYN` packet, the server responds with a `SYN/ACK` packet. This packet serves two purposes:
1. It acknowledges the receipt of the client's `SYN` request.
2. It includes the server's own **sequence number**, establishing its side of the connection.

- Purpose: Acknowledges client's request and synchronizes sequence numbers.
- Example:
  ```
  Server → Client: [SYN, ACK, SEQ = y, ACK = x + 1]
  ```

## **Step 3: ACK (Acknowledge)**
The client responds to the `SYN/ACK` packet by sending an `ACK` packet. This confirms that the client has received the server's response, completing the handshake.

- Purpose: Final confirmation of the connection.
- Example:
  ```
  Client → Server: [ACK, SEQ = x + 1, ACK = y + 1]
  ```

At this point, the connection is **fully established**, and both parties can begin transmitting data securely.

---

### **Visual Representation of the 3-Way Handshake**
```
Client          Server
   |  SYN  →    |
   |  ← SYN/ACK |
   |  ACK  →    |
Connection Established
```

### **Why is the 3-Way Handshake Important?**
- Ensures both client and server agree on initial sequence numbers.
- Prevents lost or duplicate packets from affecting communication.
- Provides a reliable foundation for TCP connections.

By using this handshake process, TCP ensures that connections are established in an organized and reliable manner before any actual data transmission occurs.

