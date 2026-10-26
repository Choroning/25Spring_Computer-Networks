# Chapter 13 — Introduction to the Transport Layer

[Repository Guide](../../README.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **Last Updated:** 2026-10-26
>
> TCP/IP Protocol Suite, Forouzan, Ch 13

> **Learning Objectives:**
> 1. Explain the role of the transport layer
> 2. Distinguish process-to-process vs host-to-host delivery
> 3. Describe port numbers and socket addressing

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
- [7. Appendix](#7-appendix)
  - [7.1 Well-Known Port Numbers](#71-well-known-port-numbers)
  - [7.2 Go-Back-N vs. Selective Repeat](#72-go-back-n-vs-selective-repeat)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Transport-Layer Services

The **transport layer** is located between the network layer and the application layer. It is responsible for providing services to the application layer and receives services from the network layer.

### 1.1 Process-to-Process Communication

While IP delivers packets to the correct **computer** (host-to-host), the transport layer delivers messages to the correct **process** (process-to-process).

```text
Processes ...                           Processes ...
 |  |  |                                 |  |  |
+--------+                             +--------+
|Transport|  <---- End-to-end ---->    |Transport|
+--------+                             +--------+
|Network  |  <---- Hop-by-hop ---->    |Network  |
+--------+       (Internet)            +--------+
  Host A                                 Host B
```

*Figure 1. End-to-end transport-layer communication and hop-by-hop network-layer delivery*

For communication, we must define four elements:
- **Local host** (IP address)
- **Local process** (port number)
- **Remote host** (IP address)
- **Remote process** (port number)

### 1.2 Port Numbers

Port numbers are **16-bit** integers (0-65,535) that identify processes:

| Range | Type | Description |
|-------|------|-------------|
| 0-1,023 | Well-Known | Assigned by IANA (HTTP=80, FTP=21, etc.) |
| 1,024-49,151 | Registered | Assigned by IANA upon request |
| 49,152-65,535 | Dynamic/Private | Assigned temporarily by OS (ephemeral ports) |

*Table 1. Port number ranges*

```text
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

*Figure 2. Daytime client and server communication using port numbers*

- The **destination port** selects the process.
- The **destination IP address** selects the server (host).

### 1.3 Socket Addresses

A **socket address** is the combination of an IP address and a port number:

```text
IP address:     200.23.56.8
Port number:    69
Socket address: 200.23.56.8:69
```

- The IP header contains the IP addresses.
- The transport-layer header (TCP or UDP) contains the port numbers.
- Together, they uniquely identify a communication endpoint within a transport protocol.

> **Key Point:** A socket address (IP:Port) uniquely identifies a process on a specific host, enabling process-to-process communication across the Internet.

> **[Systems Programming]** The socket interface studied in Systems Programming is a set of system calls through which an application process creates and uses a communication endpoint identified by such a socket address. A server attaches its well-known port to a socket with `bind`, while a client usually leaves the port unspecified, so the operating system picks an ephemeral port and attaches it at `connect` or at the first send.

---

<br>

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

*Table 2. Comparison of connectionless and connection-oriented services*

### 2.2 Reliable vs. Unreliable

| Feature | Unreliable | Reliable |
|---------|-----------|----------|
| Protocol | UDP | TCP |
| Delivery guarantee | None | Guaranteed |
| Retransmission | No | Yes |
| Error control | Checksum detection only | Checksum + ACK + retransmit |
| Duplicate detection | No | Yes |
| Order guarantee | No | Yes |

*Table 3. Comparison of unreliable and reliable protocols*

---

<br>

## 3. Flow Control

### 3.1 Pushing and Pulling

**Flow control** balances the production rate and consumption rate between information producer and consumer:

```text
a. Pushing:                    b. Pulling:
  Producer --> Consumer          Consumer <-- request --> Producer
  (sends without request)        (sends only when requested)
```

*Figure 3. Pushing and pulling delivery*

Between the application layer and transport layer:
- The **application layer (sender)** pushes data to the transport layer.
- The **application layer (receiver)** pulls data from the transport layer; that is, the receiving transport layer delivers data when the process asks for it.

**At the transport layer level:**
- The sender's transport layer pushes data to the network.
- The receiver's transport layer accepts data from the network.
- Flow control prevents the receiver from being overwhelmed.

### 3.2 Buffers

Flow control is implemented using **two buffers** (sender and receiver):
- **Sender buffer**: Stores data received from the application until it is sent.
- **Receiver buffer**: Stores data received from the network until the application consumes it.
- If the receiver buffer is full, the sender must stop sending.

---

<br>

## 4. Error Control

Error control at the transport layer is responsible for the following:
- It **detects and discards** corrupted packets.
- It **keeps track** of lost and discarded packets and **resends** them.
- It **recognizes duplicate** packets and discards them.
- It **buffers out-of-order** packets until the missing packets arrive.

### 4.1 Sequence Numbers

Packets are assigned **sequence numbers** for the following purposes:
- They identify which packet needs retransmission.
- They detect duplicate packets.
- They detect out-of-order delivery.
- Sequence numbers are **modulo $2^m$**, where $m$ is the size of the sequence number field in bits. Sequence numbers therefore run from 0 to $2^m - 1$ and then repeat.

### 4.2 Acknowledgment

**ACK (Acknowledgment)** can be:
- **Positive (ACK)**: Confirms correct receipt.
- **Negative (NAK)**: Reports corruption or loss.

ACK mechanisms:
- **Individual ACK**: Acknowledges each packet separately.
- **Cumulative ACK**: Acknowledges all packets up to a certain sequence number at once.

> **Key Point:** Sequence numbers and acknowledgments together provide the foundation for reliable data transfer over unreliable networks.

---

<br>

## 5. Combination of Flow and Error Control

### 5.1 Sliding Window

The **sliding window** protocol combines flow control and error control:

- The sender and receiver each maintain a buffer.
- The buffers are numbered using **sequence numbers** and **acknowledgment numbers**.
- The window can be represented in **circular format** or **linear format**.

```text
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

*Figure 4. Circular and linear representations of a sliding window of size 7 with sequence numbers modulo 16*

**Window operation:**
1. Initially, the window covers sequence numbers 0-6 (size 7).
2. The sender can send packets within the window without waiting for an ACK.
3. As ACKs arrive, the window slides forward.
4. If all packets in the window have been sent and no ACK has arrived, the sender must wait.

**Sender window states:**
- Packets before the window have already been sent and acknowledged.
- Packets in the left part of the window have been sent but not yet acknowledged (outstanding).
- Packets in the right part of the window have not been sent yet but can be sent.
- Packets after the window cannot be sent yet.

---

<br>

## 6. Congestion Control

**Congestion control** refers to the mechanisms and techniques to control congestion and keep the network load below capacity.

### 6.1 Open-Loop Congestion Control

Open-loop congestion control prevents congestion **before it happens**:
- It is applied by either the source or the destination.
- **Retransmission policy**: Retransmission timers are designed to optimize efficiency without adding to congestion.
- **Window policy**: The type of sender window also affects congestion. Go-Back-N (Section 7.2) can add to congestion by resending packets that already arrived safely, so Selective Repeat is better for congestion control.
- **ACK reply policy**: Timer-based or cumulative ACKs reduce the number of ACKs and thus the network load.

### 6.2 Closed-Loop Congestion Control

Closed-loop congestion control tries to alleviate congestion **after it happens**:
- The size of the sender's window can be adjusted **flexibly** according to network conditions.
- Typical mechanisms include the following:
  - **ECN (Explicit Congestion Notification)**: When routers detect congestion, they mark packets to notify the end hosts.
  - **Backpressure**: Congestion information propagates backward from the congestion point toward the source.
  - **Choke packets**: A congested node sends the source a special packet asking it to slow down.

---

<br>

## 7. Appendix

### 7.1 Well-Known Port Numbers

| Port | Protocol | Service |
|------|----------|---------|
| 7 | Echo | Echoes received datagram |
| 13 | Daytime | Returns date and time |
| 20/21 | FTP | File Transfer (data/control) |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Remote login |
| 25 | SMTP | Email sending |
| 53 | DNS | Domain Name System |
| 67/68 | DHCP | Dynamic Host Configuration |
| 69 | TFTP | Trivial File Transfer |
| 80 | HTTP | Web |
| 110 | POP3 | Email retrieval |
| 111 | RPC | Remote Procedure Call |
| 123 | NTP | Network Time Protocol |
| 143 | IMAP | Email retrieval |
| 161/162 | SNMP | Network Management |
| 443 | HTTPS | Secure Web |

*Table 4. Common well-known port numbers*

### 7.2 Go-Back-N vs. Selective Repeat

| Feature | Go-Back-N | Selective Repeat |
|---------|-----------|-----------------|
| Retransmission | All packets from lost one onward | Only the lost packet |
| Receiver buffer | 1 slot | Window size slots |
| Timer | One timer for oldest unACKed | Timer per unACKed packet |
| Complexity | Simpler | More complex |
| Efficiency | Lower (retransmits good packets) | Higher (retransmits only lost) |
| Send window size limit | $2^m - 1$ | $2^{m-1}$ |

*Table 5. Comparison of Go-Back-N and Selective Repeat*

---

<br>

## Summary

| Concept | Key Summary |
|---------|-----------|
| Transport Layer | The transport layer provides process-to-process communication between applications. |
| Port Numbers | Port numbers are 16-bit identifiers divided into well-known (0-1,023), registered, and dynamic ranges. |
| Socket Address | A socket address, the combination of an IP address and a port number, uniquely identifies a process. |
| Flow Control | Flow control uses buffers to balance the sending rate and the receiver's consumption rate. |
| Error Control | Error control detects errors using sequence numbers and ACKs and corrects them by retransmission. |
| Sliding Window | A sliding window combines flow and error control and allows multiple unacknowledged packets to be sent. |
| Congestion Control | Congestion control is divided into open-loop methods that prevent congestion and closed-loop methods that alleviate it. |

---

<br>

## Self-Check Questions

1. **Sequence numbers and window size:** Give the range of sequence numbers when the sequence number field is 4 bits. Find the maximum send window size for Go-Back-N and for Selective Repeat, and explain what goes wrong if the Go-Back-N window size is 16.

   <details>
   <summary>Answer</summary>

   Sequence numbers are modulo $2^4 = 16$, so they range over 0-15. The maximum send window size is $2^4 - 1 = 15$ for Go-Back-N and $2^{4-1} = 8$ for Selective Repeat. If the Go-Back-N window were 16, the sender would send packets using all 16 sequence numbers, and if all ACKs were lost, it would resend packet 0. The receiver has already received all 16 and is waiting for packet 0 of the next cycle, so it wrongly accepts the old duplicate packet 0 as a new one.

   </details>

2. **Tracing a sliding window:** Sequence numbers are modulo 16, and the send window size is 7. The window covers sequence numbers 12, 13, 14, 15, 0, 1, 2. The sender has sent 12, 13, 14, 15, 0, 1, and a cumulative ACK acknowledging 12, 13, and 14 arrives. After the window slides, give the sequence numbers it covers, the outstanding packets, and the packets that can be sent now.

   <details>
   <summary>Answer</summary>

   Three packets are acknowledged, so the window slides three positions and covers 15, 0, 1, 2, 3, 4, 5. Of these, the outstanding packets, which were sent but not yet acknowledged, are 15, 0, and 1. The four packets not yet sent, 2, 3, 4, and 5, can be sent immediately without waiting for an ACK. Because sequence numbers return to 0 after 15, the window also wraps around.

   </details>

3. **Retransmitting a lost packet:** A sender sends packets 0-6 back to back, and only packet 2 is lost. For Go-Back-N and Selective Repeat, give the packets that are retransmitted and how many there are.

   <details>
   <summary>Answer</summary>

   A Go-Back-N receiver accepts only packets that arrive in order, so it discards 3-6, which arrive while it is waiting for 2. When the timer for packet 2 expires, the sender therefore retransmits five packets: 2, 3, 4, 5, and 6. A Selective Repeat receiver buffers these four packets, so the sender retransmits only the lost packet 2.

   </details>

4. **Port numbers and socket addresses:** State which range each of ports 53, 1,023, 8,080, 49,152, and 52,000 belongs to. Also explain how a server distinguishes two connections when two client processes on host 10.0.0.1 connect to the same web server 200.23.56.8:80 at the same time.

   <details>
   <summary>Answer</summary>

   According to Table 1, ports 53 and 1,023 are in the well-known range, 8,080 is in the registered range, and 49,152 and 52,000 are in the dynamic range. Port 1,023 is the last number of the well-known range, and 49,152 is the first number of the dynamic range. The two client processes receive different ephemeral ports from the operating system (for example, 52,000 and 52,001), so the client socket addresses of the two connections differ: 10.0.0.1:52000 and 10.0.0.1:52001. Of the four elements (local host, local process, remote host, and remote process), the server distinguishes the two connections by the different port number of the remote process.

   </details>
