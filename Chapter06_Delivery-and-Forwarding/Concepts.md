# Chapter 06 -- Delivery and Forwarding of IP Packets

> **Last Updated:** 2026-03-21

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
- [Summary](#summary)
- [Appendix](#appendix)

---

## 1. Delivery

The network layer supervises delivery. The delivery of a packet to its final destination is accomplished using two methods: **direct** and **indirect** delivery.

### 1.1 Direct Delivery

**Direct delivery** occurs when the destination host is on the **same physical network** as the sender:

```
         Link
Host A ----------- Host B
    \              /
     \  Switch    /
      +---------+
```

Key characteristics:
- The source and destination are on the **same network**
- Performed between the **last router and the destination host**
- The sender extracts the **network address (netid)** from the destination address and compares it with its own network address
- If they match, direct delivery is performed

### 1.2 Indirect Delivery

**Indirect delivery** occurs when the destination host is on a **different network**:

```
  A                                              B
[Host] --- Switch --- Router --- Router --- Switch --- [Host]
  |                     |          |                    |
  +-- Indirect Delivery +          +-- Direct Delivery -+
```

Key characteristics:
- The destination is **not on the same network** as the sender
- The packet passes through **multiple routers**
- The **routing table** is used to find the next-hop IP address
- The last delivery is always a direct delivery

> **Key Point:** In indirect delivery, the sender and intermediate routers pass the packet from one router to the next. Only the final delivery (from the last router to the destination host) is direct.

---

## 2. Forwarding

**Forwarding** means placing the packet on its route to its destination. Forwarding requires a host or router to have a **routing table**.

### 2.1 Forwarding Techniques

Four techniques simplify the routing table and the forwarding process:

**1. Next-Hop Method:**
- The routing table holds only the address of the **next hop** instead of the complete route
- Reduces table size and simplifies the forwarding process

```
Route-Based Table:              Next-Hop Table:
+------+------------------+     +------+---------+
| Dest | Route             |    | Dest | Next Hop|
+------+------------------+     +------+---------+
|  B   | R1, R2, Host B   |    |  B   |   R1    |
+------+------------------+     +------+---------+
```

**2. Network-Specific Method:**
- Instead of having an entry for **every destination host**, use one entry for the **destination network**
- Dramatically reduces routing table size

```
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

**3. Host-Specific Method:**
- The routing table contains entries for **specific destination hosts**
- Used when a specific route to a particular host is needed (e.g., for security or special handling)
- Inverse of the network-specific method

**4. Default Method:**
- Instead of listing all networks, use a single **default entry (0.0.0.0)**
- Packets that do not match any specific entry are sent to the default router

### 2.2 Forwarding with Classful Addressing

In classful addressing, a router has three tables (one each for Class A, B, and C).

Each routing table entry has a minimum of three columns:

| Column | Description |
|--------|-------------|
| Network Address | The network where the destination host is located |
| Next-Hop Address | The router to which the packet must be delivered for indirect delivery |
| Interface Number | The outgoing port (m0, m1, etc.) |

**Forwarding process (classful):**
1. Extract the destination IP address from the packet header
2. Determine the class (A, B, or C) from the first few bits
3. Apply the class-specific default mask to extract the network address
4. Search the appropriate table for the network address
5. If found, forward to the next-hop address via the specified interface
6. If not found, use the default entry

### 2.3 Forwarding with Classless Addressing (CIDR)

In classless addressing, there is **one table** that contains the network address (prefix) with its mask:

```
+------------------+------+-----------+-----------+
| Network/Prefix   | Mask | Next Hop  | Interface |
+------------------+------+-----------+-----------+
| 192.168.1.0/24   | /24  | R1        | m0        |
| 10.0.0.0/8       | /8   | R2        | m1        |
| 0.0.0.0/0        | /0   | R3        | m2        |  <-- Default
+------------------+------+-----------+-----------+
```

**Forwarding process (classless):**
1. Extract destination address
2. For each entry in the table, apply the mask (AND operation) to the destination address
3. If the result matches the network address, this is a potential match
4. Apply **longest prefix match** to select the best route
5. Forward to the corresponding next-hop

---

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

### 3.2 Address Aggregation

Address aggregation (supernetting) reduces routing table entries:

```
Before aggregation:          After aggregation:
192.168.0.0/24  --> R1       192.168.0.0/22 --> R1
192.168.1.0/24  --> R1       (single entry replaces four)
192.168.2.0/24  --> R1
192.168.3.0/24  --> R1
```

> **Key Point:** Aggregation works only when the networks are contiguous and share the same next hop. This is fundamental to Internet scalability.

### 3.3 Longest Prefix Match

When multiple routing table entries match a destination address, the entry with the **longest prefix** (most specific match) is selected:

```
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

## Summary

| Concept | Key Point |
|---------|-----------|
| Direct Delivery | Source and destination on same network; last hop is always direct |
| Indirect Delivery | Packet passes through routers; uses routing tables for next-hop |
| Next-Hop Method | Store only next router, not complete path |
| Network-Specific | One entry per network, not per host |
| Default Route | Catch-all entry (0.0.0.0/0) for unknown destinations |
| Classful Forwarding | Separate tables per class; extract netid using class mask |
| Classless Forwarding | Single table with prefix/mask; AND operation for matching |
| Longest Prefix Match | Most specific (longest prefix) matching entry wins |
| Address Aggregation | Combine contiguous networks to reduce table size |

---

## Appendix

### A. Example: Classful Forwarding

Given destination IP: 192.168.5.100

1. First 3 bits are `110` --> Class C
2. Default mask: 255.255.255.0 (/24)
3. Network address: 192.168.5.0
4. Search Class C routing table for 192.168.5.0
5. If found, forward to the indicated next hop
6. If not found, use default route

### B. Example: Classless Forwarding

Given destination IP: 10.1.2.100 and routing table:

| Network | Mask | Next Hop |
|---------|------|----------|
| 10.1.0.0 | /16 | R1 |
| 10.1.2.0 | /24 | R2 |
| 0.0.0.0 | /0 | R3 |

1. 10.1.2.100 AND /16 = 10.1.0.0 --> Match (R1)
2. 10.1.2.100 AND /24 = 10.1.2.0 --> Match (R2)
3. 10.1.2.100 AND /0 = 0.0.0.0 --> Match (R3)
4. Longest prefix match: /24 --> Forward to **R2**

### C. Real-World Routing Table (Linux)

```
$ ip route show
default via 192.168.1.1 dev eth0
10.0.0.0/8 via 10.0.0.1 dev eth1
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```
