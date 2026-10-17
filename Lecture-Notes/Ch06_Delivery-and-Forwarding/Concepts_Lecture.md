# Chapter 6 — Delivery and Forwarding of IP Packets

[Repository Guide](../../README.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **Last Updated:** 2026-10-17
>
> TCP/IP Protocol Suite, Forouzan, Ch 6

> **Learning Objectives:**
> 1. Distinguish direct and indirect delivery of packets
> 2. Explain forwarding table lookup and longest prefix matching
> 3. Describe routing table structure and next-hop determination

---

## Table of Contents

- [1. Delivery](#1-delivery)
  - [1.1 Direct Delivery](#11-direct-delivery)
  - [1.2 Indirect Delivery](#12-indirect-delivery)
- [2. Forwarding](#2-forwarding)
  - [2.1 Forwarding Techniques](#21-forwarding-techniques)
  - [2.2 Forwarding with Classful Addressing](#22-forwarding-with-classful-addressing)
  - [2.3 Forwarding with Classless Addressing (CIDR)](#23-forwarding-with-classless-addressing-cidr)
- [3. Routing Table Structure](#3-routing-table-structure)
  - [3.1 Routing Table Columns](#31-routing-table-columns)
  - [3.2 Address Aggregation](#32-address-aggregation)
  - [3.3 Longest Prefix Match](#33-longest-prefix-match)
- [4. Appendix](#4-appendix)
  - [4.1 Example: Classful Forwarding](#41-example-classful-forwarding)
  - [4.2 Example: Classless Forwarding](#42-example-classless-forwarding)
  - [4.3 Real-World Routing Table (Linux)](#43-real-world-routing-table-linux)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Delivery

The network layer supervises delivery. The delivery of a packet to its final destination is accomplished using two methods: **direct** and **indirect** delivery.

### 1.1 Direct Delivery

**Direct delivery** occurs when the destination host is on the **same physical network** as the sender:

```text
         Link
Host A ----------- Host B
    \              /
     \  Switch    /
      +---------+
```

*Figure 1. Direct delivery between two hosts on the same network*

Key characteristics:
- It is performed when the source and destination are on the **same network**.
- If they are on different networks, it is performed between the **last router and the destination host**.
- The sender extracts the **network address (netid)** from the destination address and compares it with its own network address.
- If they match, direct delivery is performed.

### 1.2 Indirect Delivery

**Indirect delivery** occurs when the destination host is on a **different network**:

```text
  A                                              B
[Host] --- Switch --- Router --- Router --- Switch --- [Host]
  |                     |          |                    |
  +-- Indirect Delivery +          +-- Direct Delivery -+
```

*Figure 2. Indirect delivery through routers followed by a final direct delivery*

Key characteristics:
- The destination is **not on the same network** as the sender.
- The packet passes through **one or more routers**.
- The **routing table** is used to find the next-hop IP address.
- The last delivery is always a direct delivery.

> **Key Point:** In indirect delivery, the sender and intermediate routers pass the packet from one router to the next. Only the final delivery (from the last router to the destination host) is direct.

---

<br>

## 2. Forwarding

**Forwarding** means placing the packet on its route to its destination. Forwarding requires a host or router to have a **routing table**.

### 2.1 Forwarding Techniques

Four forwarding techniques keep the routing table at a manageable size or handle special requirements:

**1. Next-Hop Method:**
- The routing table holds only the address of the **next hop** instead of the complete route.
- It reduces table size and simplifies the forwarding process.

```text
Route-Based Table:              Next-Hop Table:
+------+------------------+     +------+---------+
| Dest | Route             |    | Dest | Next Hop|
+------+------------------+     +------+---------+
|  B   | R1, R2, Host B   |    |  B   |   R1    |
+------+------------------+     +------+---------+
```

*Figure 3. Route-based table and next-hop table*

**2. Network-Specific Method:**
- Instead of having an entry for **every destination host**, the table uses one entry for the **destination network**.
- It dramatically reduces routing table size.

```text
Host-Specific Table:            Network-Specific Table:
+------+---------+              +------+---------+
| Dest | Next Hop|              | Dest | Next Hop|
+------+---------+              +------+---------+
|  A   |   R1    |              |  N2  |   R1    |
|  B   |   R1    |              +------+---------+
|  C   |   R1    |
|  D   |   R1    |
+------+---------+
```

*Figure 4. Host-specific table and network-specific table*

**3. Host-Specific Method:**
- The routing table contains entries for **specific destination hosts**.
- It is used when a specific route to a particular host is needed (e.g., for security or special handling).
- It is the inverse of the network-specific method.

**4. Default Method:**
- Instead of listing all networks, the table uses a single **default entry (0.0.0.0)**.
- Packets that do not match any specific entry are sent to the default router.

### 2.2 Forwarding with Classful Addressing

In classful addressing, a router has three tables (one each for Class A, B, and C).

Each routing table entry has a minimum of three columns:

| Column | Description |
|--------|-------------|
| Network Address | The network where the destination host is located |
| Next-Hop Address | The router to which the packet must be delivered for indirect delivery |
| Interface Number | The outgoing port (m0, m1, etc.) |

*Table 1. Minimum columns of a classful routing table entry*

**Forwarding process (classful):**
1. Extract the destination IP address from the packet header.
2. Determine the class (A, B, or C) from the first few bits.
3. Apply the class-specific default mask to extract the network address.
4. Search the table for that class for the network address.
5. If found, forward to the next-hop address via the specified interface.
6. If not found, use the default entry.

### 2.3 Forwarding with Classless Addressing (CIDR)

In classless addressing, there is **one table** that contains the network address (prefix) with its mask:

```text
+------------------+------+-----------+-----------+
| Network/Prefix   | Mask | Next Hop  | Interface |
+------------------+------+-----------+-----------+
| 192.168.1.0/24   | /24  | R1        | m0        |
| 10.0.0.0/8       | /8   | R2        | m1        |
| 0.0.0.0/0        | /0   | R3        | m2        |  <-- Default
+------------------+------+-----------+-----------+
```

*Figure 5. Classless forwarding table with masks and a default route*

**Forwarding process (classless):**
1. Extract the destination address.
2. For each entry in the table, apply that entry's mask (AND operation) to the destination address.
3. If the result matches the entry's network address, the entry is a candidate.
4. Apply **longest prefix match** to select the best route.
5. Forward to the corresponding next hop.

---

<br>

## 3. Routing Table Structure

### 3.1 Routing Table Columns

A typical routing table contains:

| Column | Description |
|--------|-------------|
| Destination Network | Network address with prefix length |
| Subnet Mask | Mask for the destination network |
| Next Hop | IP address of the next router (or "directly connected") |
| Interface | Outgoing interface identifier |
| Metric | Cost/distance to the destination |
| Flags | Route type indicators (U=up, G=gateway, H=host, etc.) |

*Table 2. Columns of a typical routing table*

### 3.2 Address Aggregation

Address aggregation (supernetting) reduces routing table entries:

```text
Before aggregation:          After aggregation:
192.168.0.0/24  --> R1       192.168.0.0/22 --> R1
192.168.1.0/24  --> R1       (single entry replaces four)
192.168.2.0/24  --> R1
192.168.3.0/24  --> R1
```

*Figure 6. Routing entries before and after aggregating four /24 entries into one /22*

> **Key Point:** Aggregation works only when the networks are contiguous, together form a single CIDR block, and share the same next hop. This is fundamental to Internet scalability.

### 3.3 Longest Prefix Match

When multiple routing table entries match a destination address, the entry with the **longest prefix** (most specific match) is selected:

```text
Table:
  192.168.0.0/16   --> R1
  192.168.1.0/24   --> R2
  192.168.1.128/25 --> R3

For destination 192.168.1.200:
  /16 matches (192.168.x.x)     --> R1
  /24 matches (192.168.1.x)     --> R2
  /25 matches (192.168.1.128+)  --> R3  <-- SELECTED (longest prefix)
```

> **Key Point:** Longest prefix match ensures the most specific route is used, allowing both aggregation and specific exception routes to coexist.

---

<br>

## 4. Appendix

### 4.1 Example: Classful Forwarding

Given destination IP address 192.168.5.100:

1. The first 3 bits are `110`, so the address is Class C.
2. The default mask is 255.255.255.0 (/24).
3. The network address is 192.168.5.0.
4. Search the Class C routing table for 192.168.5.0.
5. If found, forward to the indicated next hop.
6. If not found, use the default route.

### 4.2 Example: Classless Forwarding

Given destination IP address 10.1.2.100 and the following routing table:

| Network | Mask | Next Hop |
|---------|------|----------|
| 10.1.0.0 | /16 | R1 |
| 10.1.2.0 | /24 | R2 |
| 0.0.0.0 | /0 | R3 |

*Table 3. Routing table for the classless forwarding example*

1. 10.1.2.100 AND /16 = 10.1.0.0 --> Match (R1)
2. 10.1.2.100 AND /24 = 10.1.2.0 --> Match (R2)
3. 10.1.2.100 AND /0 = 0.0.0.0 --> Match (R3)
4. By longest prefix match, the /24 entry is selected and the packet is forwarded to **R2**.

### 4.3 Real-World Routing Table (Linux)

```console
$ ip route show
default via 192.168.1.1 dev eth0
10.0.0.0/8 via 10.0.0.1 dev eth1
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

---

<br>

## Summary

| Concept | Key Summary |
|---------|-----------|
| Direct Delivery | It occurs when the source and destination are on the same network, and the last hop is always a direct delivery. |
| Indirect Delivery | The packet passes through routers, which use routing tables to find the next hop. |
| Next-Hop Method | The table stores only the address of the next router, not the complete path. |
| Network-Specific | The table has one entry per network, not one per host. |
| Default Route | It is a catch-all entry (0.0.0.0/0) for destinations not in the table. |
| Classful Forwarding | Each class has a separate table, and the netid is extracted with the class default mask. |
| Classless Forwarding | A single table holds prefixes and masks, and entries are matched with the AND operation. |
| Longest Prefix Match | Among the matching entries, the most specific (longest prefix) entry wins. |
| Address Aggregation | It combines contiguous networks to reduce table size. |

---

<br>

## Self-Check Questions

1. **Direct and indirect delivery:** Host 192.168.10.37/26 sends packets to destinations 192.168.10.70 and 192.168.10.12. Decide whether each case is a direct or an indirect delivery.

   <details>
   <summary>Answer</summary>

   The mask for /26 is 255.255.255.192. Since 37 AND 192 = 0, the sender's network address is 192.168.10.0. Since 70 AND 192 = 64, the network address of 192.168.10.70 is 192.168.10.64, which differs from the sender's network, so this is an indirect delivery (the packet goes to the default router). Since 12 AND 192 = 0, 192.168.10.12 is on the same network, so this is a direct delivery.

   </details>

2. **Longest prefix match:** A routing table sends 130.40.0.0/16 to R1, 130.40.32.0/19 to R2, 130.40.36.0/22 to R3, and 0.0.0.0/0 to R4. Find the next hop for destinations (a) 130.40.38.5 (b) 130.40.50.1 (c) 130.41.0.1.

   <details>
   <summary>Answer</summary>

   (a) The third octet 38 = 00100110 ANDed with 224, the third octet of the /19 mask, gives 32, and ANDed with 252, the third octet of the /22 mask, gives 36. All four entries match, so the /22 entry with the longest prefix is selected and the next hop is R3. (b) Since 50 AND 224 = 32, the /19 entry matches, but since 50 AND 252 = 48, the /22 entry does not. The next hop is R2. (c) 130.41.0.1 AND 255.255.0.0 = 130.41.0.0 differs from 130.40.0.0, so only the default route matches and the next hop is R4.

   </details>

3. **Aggregation and exception routes:** A router sends all eight networks from 172.20.16.0/24 to 172.20.23.0/24 to R1. Aggregate these entries into one. If only 172.20.20.0/24 must go to R2, how should the table be built?

   <details>
   <summary>Answer</summary>

   The third octets 16-23 are 00010000-00010111 in binary and share the first 5 bits 00010. The common prefix is 16 + 5 = 21 bits, and 16 is a multiple of 8, so the entries aggregate into a single entry 172.20.16.0/21 with next hop R1. To handle the exception, add an entry 172.20.20.0/24 with next hop R2. Packets to 172.20.20.x match both entries, but longest prefix match sends them to R2 through the /24 entry, and packets to the other seven networks go to R1 through the /21 entry.

   </details>

4. **Classful forwarding:** A classful router receives a packet for destination 150.25.7.9. In which class table does it search, and for which network address?

   <details>
   <summary>Answer</summary>

   150 = 10010110 starts with the bits 10, so the address is Class B. Applying the default mask 255.255.0.0 gives the network address 150.25.0.0, which the router searches for in the Class B table.

   </details>
