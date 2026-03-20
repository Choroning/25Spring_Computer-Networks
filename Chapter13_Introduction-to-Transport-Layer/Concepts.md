# Chapter 13 -- Introduction to the Transport Layer

> **Last Updated:** 2026-03-21

---

## Table of Contents

- [1. Transport-Layer Services](#1-transport-layer-services)
  - [1.1 Process-to-Process Communication](#11-process-to-process-communication)
  - [1.2 Port Numbers](#12-port-numbers)
  - [1.3 Socket Addresses](#13-socket-addresses)
- [2. Transport-Layer Protocols](#2-transport-layer-protocols)
  - [2.1 Connectionless vs. Connection-Oriented](#21-connectionless-vs-connection-oriented)
  - [2.2 Reliable vs. Unreliable](#22-reliable-vs-unreliable)
- [3. Flow Control](#3-flow-control)
  - [3.1 Pushing and Pulling](#31-pushing-and-pulling)
  - [3.2 Buffers](#32-buffers)
- [4. Error Control](#4-error-control)
  - [4.1 Sequence Numbers](#41-sequence-numbers)
  - [4.2 Acknowledgment](#42-acknowledgment)
- [5. Combination of Flow and Error Control](#5-combination-of-flow-and-error-control)
  - [5.1 Sliding Window](#51-sliding-window)
- [6. Congestion Control](#6-congestion-control)
  - [6.1 Open-Loop Congestion Control](#61-open-loop-congestion-control)
  - [6.2 Closed-Loop Congestion Control](#62-closed-loop-congestion-control)
- [Summary](#summary)
- [Appendix](#appendix)

---

## 1. Transport-Layer Services

The **transport layer** is located between the network layer and the application layer. It is responsible for providing services to the application layer and receives services from the network layer.

### 1.1 Process-to-Process Communication

While IP delivers packets to the correct **computer** (host-to-host), the transport layer delivers messages to the correct **process** (process-to-process).

```
Processes ...                           Processes ...
 |  |  |                                 |  |  |
+--------+                             +--------+
|Transport|  <---- End-to-end ---->    |Transport|
+--------+                             +--------+
|Network  |  <---- Hop-by-hop ---->    |Network  |
+--------+       (Internet)            +--------+
  Host A                                 Host B
```

For communication, we must define four elements:
- **Local host** (IP address)
- **Local process** (port number)
- **Remote host** (IP address)
- **Remote process** (port number)

### 1.2 Port Numbers

Port numbers are **16-bit** integers (0 to 65,535) that identify processes:

| Range | Type | Description |
|-------|------|-------------|
| 0--1,023 | Well-Known | Assigned by IANA (HTTP=80, FTP=21, etc.) |
| 1,024--49,151 | Registered | Assigned by IANA upon request |
| 49,152--65,535 | Dynamic/Private | Assigned temporarily by OS (ephemeral ports) |

```
Daytime                              Daytime
client                               server
  |                                    |
  | Port 52,000                        | Port 13
  +--------+                        +--------+
  |Transport|                        |Transport|
  +--------+                        +--------+
  |  52,000 | 13 |   Data   |  -->  |   13  |
  +--------+                        +--------+
```

- The **destination port** selects the process
- The **destination IP address** selects the server (host)

### 1.3 Socket Addresses

A **socket address** is the combination of an IP address and a port number:

```
IP address:     200.23.56.8
Port number:    69
Socket address: 200.23.56.8:69
```

- The IP header contains the IP addresses
- The transport header (TCP/UDP) contains the port numbers
- Together, they uniquely identify a communication endpoint

> **Key Point:** A socket address (IP:Port) uniquely identifies a process on a specific host, enabling process-to-process communication across the Internet.

---

## 2. Transport-Layer Protocols

### 2.1 Connectionless vs. Connection-Oriented

| Feature | Connectionless | Connection-Oriented |
|---------|---------------|-------------------|
| Protocol | UDP | TCP |
| Connection setup | No | Yes (three-way handshake) |
| Packet independence | Each independent | Part of a stream |
| Ordering | Not guaranteed | Guaranteed |
| Overhead | Low | Higher |
| Use cases | DNS, streaming, gaming | Web, email, file transfer |

### 2.2 Reliable vs. Unreliable

| Feature | Unreliable | Reliable |
|---------|-----------|----------|
| Protocol | UDP | TCP |
| Delivery guarantee | None | Guaranteed |
| Retransmission | No | Yes |
| Error detection | Checksum only | Checksum + ACK + retransmit |
| Duplicate detection | No | Yes |
| Order guarantee | No | Yes |

---

## 3. Flow Control

### 3.1 Pushing and Pulling

**Flow control** balances the production rate and consumption rate between information producer and consumer:

```
a. Pushing:                    b. Pulling:
  Producer --> Consumer          Consumer <-- request --> Producer
  (sends without request)        (sends only when requested)
```

Between the application layer and transport layer:
- **Application layer (sender)** pushes data to transport layer
- **Transport layer (receiver)** pulls data to deliver to application layer

**At the transport layer level:**
- Sender's transport layer pushes data to the network
- Receiver's transport layer accepts data from the network
- Flow control prevents the receiver from being overwhelmed

### 3.2 Buffers

Flow control is implemented using **two buffers** (sender and receiver):
- **Sender buffer**: Stores data received from the application until sent
- **Receiver buffer**: Stores data received from the network until consumed by the application
- If the receiver buffer is full, the sender must stop sending

---

## 4. Error Control

Error control at the transport layer is responsible for:
- **Detecting and discarding** corrupted packets
- **Keeping track** of lost and discarded packets and **resending** them
- **Recognizing duplicate** packets and discarding them
- **Buffering out-of-order** packets until the missing packets arrive

### 4.1 Sequence Numbers

Packets are assigned **sequence numbers** to:
- Identify which packet needs retransmission
- Detect duplicate packets
- Detect out-of-order delivery
- Sequence numbers are **modulo 2^m** where m is the size of the sequence number field in bits

### 4.2 Acknowledgment

**ACK (Acknowledgment)** can be:
- **Positive (ACK)**: Confirms correct receipt
- **Negative (NAK)**: Reports corruption or loss

ACK mechanisms:
- **Individual ACK**: Acknowledges each packet separately
- **Cumulative ACK**: Acknowledges all packets up to a certain sequence number

> **Key Point:** Sequence numbers and acknowledgments together provide the foundation for reliable data transfer over unreliable networks.

---

## 5. Combination of Flow and Error Control

### 5.1 Sliding Window

The **sliding window** protocol combines flow control and error control:

- Sender and receiver each maintain a buffer
- Buffers are numbered using **sequence numbers** and **acknowledgment numbers**
- Can be represented in **circular format** or **linear format**

```
Sequence numbers: modulo 16 (4-bit field)
Window size: 7

Circular representation:
         0
      15   1
    14       2
   13         3
  12    [Window]  4
   11         5
    10       6
      9    7
         8

Linear representation:
|12|13|14|15| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10|11|
              |<--- Window (size 7) --->|
```

**Window operation:**
1. Initially, window covers positions 0 through 6 (size 7)
2. Sender can send packets within the window without waiting for ACK
3. As ACKs arrive, the window slides forward
4. If the window is full (all sent, none ACKed), sender must wait

**Sender window states:**
- Packets before window: Already sent and acknowledged
- Packets in window, left side: Sent but not yet acknowledged (outstanding)
- Packets in window, right side: Can be sent
- Packets after window: Cannot be sent yet

---

## 6. Congestion Control

**Congestion control** refers to the mechanisms and techniques to control congestion and keep the network load below capacity.

### 6.1 Open-Loop Congestion Control

Prevents congestion **before it happens**:
- Applied by either the source or the destination
- **Retransmission policy**: Retransmission timer management
- **Window policy**: Selective Repeat or Go-Back-N for congestion control
- **ACK reply policy**: Timer-based and cumulative ACK

### 6.2 Closed-Loop Congestion Control

Tries to alleviate congestion **after it happens**:
- The size of the sender's window can be **flexible** (adjusted based on network conditions)
- Mechanisms include:
  - **ECN (Explicit Congestion Notification)**: Routers mark packets when congestion is detected
  - **Backpressure**: Congestion information flows backward from congestion point
  - **Choke packets**: Special packets sent to the source to slow down

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Transport Layer | Process-to-process communication between applications |
| Port Numbers | 16-bit identifiers: well-known (0-1023), registered, dynamic |
| Socket Address | IP address + port number uniquely identifies a process |
| Flow Control | Balances sender and receiver speeds using buffers |
| Error Control | Detects/corrects errors using sequence numbers and ACKs |
| Sliding Window | Combines flow and error control; allows multiple outstanding packets |
| Congestion Control | Open-loop (prevention) and closed-loop (mitigation) |

---

## Appendix

### A. Well-Known Port Numbers

| Port | Protocol | Service |
|------|----------|---------|
| 7 | Echo | Echoes received datagram |
| 13 | Daytime | Returns date and time |
| 20/21 | FTP | File Transfer (data/control) |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Remote login |
| 25 | SMTP | Email sending |
| 53 | DNS | Domain Name Service |
| 67/68 | DHCP | Dynamic Host Configuration |
| 69 | TFTP | Trivial File Transfer |
| 80 | HTTP | Web |
| 110 | POP3 | Email retrieval |
| 111 | RPC | Remote Procedure Call |
| 123 | NTP | Network Time Protocol |
| 143 | IMAP | Email retrieval |
| 161/162 | SNMP | Network Management |
| 443 | HTTPS | Secure Web |

### B. Go-Back-N vs. Selective Repeat

| Feature | Go-Back-N | Selective Repeat |
|---------|-----------|-----------------|
| Retransmission | All packets from lost one onward | Only the lost packet |
| Receiver buffer | 1 slot | Window size slots |
| Timer | One timer for oldest unACKed | Timer per unACKed packet |
| Complexity | Simpler | More complex |
| Efficiency | Lower (retransmits good packets) | Higher (retransmits only lost) |
| Window size limit | 2^m - 1 | 2^(m-1) |
