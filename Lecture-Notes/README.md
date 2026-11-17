# Lecture Notes

[Repository Guide](../README.md) | [English](README.md) | [한국어](README.ko.md)

> **Last Updated:** 2026-11-18

Each part corresponds to the chapter of the same number in Computer Networking: A Top-Down Approach.

## Part 1 Computer Networks and the Internet

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 1 Computer Networks and the Internet](Ch01_Computer-Networks-and-the-Internet/) | Components and services of the Internet, protocols and standards, the network edge and access networks, physical media, packet and circuit switching, the network of networks and the ISP hierarchy, delay, loss, and throughput, network attacks, history of the Internet | [Lecture notes](Ch01_Computer-Networks-and-the-Internet/Concepts_Lecture.md) |
| [Chapter 2 Protocol Layers and Network Models](Ch02_Protocol-Layers-and-Network-Models/) | Protocol layering, the OSI model, the TCP/IP protocol suite, comparison of the OSI model and TCP/IP, four levels of addresses, encapsulation and decapsulation, multiplexing and demultiplexing | [Lecture notes](Ch02_Protocol-Layers-and-Network-Models/Concepts_Lecture.md) |

## Part 2 Application Layer

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 3 Network Applications and the Web](Ch03_Network-Applications-and-the-Web/) | Client-server and P2P architectures, processes and sockets, iterative and concurrent servers, transport services that applications need, types of web documents, HTTP connections and message formats, cookies, web caching and the conditional GET, HTTP/2 | [Lecture notes](Ch03_Network-Applications-and-the-Web/Concepts_Lecture.md) |
| [Chapter 4 Electronic Mail, Remote Login, and File Transfer](Ch04_Electronic-Mail-Remote-Login-and-File-Transfer/) | Architecture of electronic mail, SMTP, comparison of SMTP and HTTP, MIME, POP3 and IMAP, TELNET and SSH, FTP and TFTP | [Lecture notes](Ch04_Electronic-Mail-Remote-Login-and-File-Transfer/Concepts_Lecture.md) |
| [Chapter 5 Domain Name System (DNS)](Ch05_Domain-Name-System/) | DNS services, the domain name space, hierarchical DNS servers and zones, recursive and iterative queries, DNS caching, resource records and DNS messages, record registration and DDNS, DNS security | [Lecture notes](Ch05_Domain-Name-System/Concepts_Lecture.md) |

## Part 3 Transport Layer

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 6 Transport-Layer Services and UDP](Ch06_Transport-Layer-Services-and-UDP/) | Role of the transport layer, process-to-process communication, port numbers and socket addresses, multiplexing and demultiplexing, connectionless and connection-oriented services, the user datagram format, the UDP checksum, UDP applications, the UDP package | [Lecture notes](Ch06_Transport-Layer-Services-and-UDP/Concepts_Lecture.md) |
| [Chapter 7 Principles of Reliable Data Transfer](Ch07_Principles-of-Reliable-Data-Transfer/) | Flow control and error control, rdt protocols, the stop-and-wait protocol, pipelining, Go-Back-N, Selective Repeat, sequence-number space and window size, piggybacking | [Lecture notes](Ch07_Principles-of-Reliable-Data-Transfer/Concepts_Lecture.md) |
| [Chapter 8 Transmission Control Protocol (TCP)](Ch08_Transmission-Control-Protocol/) | TCP services, the numbering system, the segment format, connection setup and teardown, the state transition diagram, windows in TCP, flow control, error control, RTT estimation and timers, options, the TCP package | [Lecture notes](Ch08_Transmission-Control-Protocol/Concepts_Lecture.md) |
| [Chapter 9 Congestion Control](Ch09_Congestion-Control/) | Causes and costs of congestion, end-to-end and network-assisted congestion control, open-loop and closed-loop congestion control, slow start, congestion avoidance, fast recovery, AIMD and TCP throughput, fairness, ECN | [Lecture notes](Ch09_Congestion-Control/Concepts_Lecture.md) |

## Part 4 The Network Layer: Data Plane

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 10 Network Layer Overview](Ch10_Network-Layer-Overview/) | Forwarding and routing, data and control planes, network service models, datagram and virtual-circuit approaches, an example of network-layer services, other network-layer issues | [Lecture notes](Ch10_Network-Layer-Overview/Concepts_Lecture.md) |
| [Chapter 11 Internet Protocol Version 4 (IPv4)](Ch11_Internet-Protocol-IPv4/) | The IPv4 datagram format, fragmentation and reassembly, path MTU discovery, options, the header checksum, security of IP, the IP package | [Lecture notes](Ch11_Internet-Protocol-IPv4/Concepts_Lecture.md) |
| [Chapter 12 IPv4 Addresses](Ch12_IPv4-Addresses/) | Address notation, bitwise operations, interfaces and subnets, classful addressing, classless addressing (CIDR), subnetting and supernetting, allocation and aggregation of address blocks, special addresses, DHCP, NAT | [Lecture notes](Ch12_IPv4-Addresses/Concepts_Lecture.md) |
| [Chapter 13 Delivery, Forwarding, and Router Architecture](Ch13_Delivery-Forwarding-and-Router-Architecture/) | Direct and indirect delivery, forwarding techniques, classful and classless forwarding, longest prefix matching, address aggregation and hierarchical routing, label-based forwarding and MPLS, router architecture, packet scheduling | [Lecture notes](Ch13_Delivery-Forwarding-and-Router-Architecture/Concepts_Lecture.md) |

## Part 5 The Network Layer: Control Plane

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 14 Routing Algorithms](Ch14_Routing-Algorithms/) | The graph model of routing, link-state routing and Dijkstra's algorithm, distance-vector routing and the Bellman-Ford equation, the count-to-infinity problem, split horizon and poisoned reverse, comparison of the two algorithms | [Lecture notes](Ch14_Routing-Algorithms/Concepts_Lecture.md) |
| [Chapter 15 Internet Routing Protocols](Ch15_Internet-Routing-Protocols/) | Autonomous systems and hierarchical routing, RIP, OSPF, path-vector routing, BGP, IP anycast, the SDN control plane and OpenFlow | [Lecture notes](Ch15_Internet-Routing-Protocols/Concepts_Lecture.md) |
| [Chapter 16 ICMPv4 and IGMP](Ch16_ICMPv4-and-IGMP/) | The ICMP message format, error-reporting messages, query messages, the ICMP checksum, ping and traceroute, the ICMP package, ICMP and security, multicast addresses, IGMP | [Lecture notes](Ch16_ICMPv4-and-IGMP/Concepts_Lecture.md) |
| [Chapter 17 Network Management and SNMP](Ch17_Network-Management-and-SNMP/) | Components of network management, managers and agents, SMI and BER encoding, MIB, SNMP | [Lecture notes](Ch17_Network-Management-and-SNMP/Concepts_Lecture.md) |

## Part 6 The Link Layer and LANs

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 18 Link Layer, Error Detection, and Multiple Access](Ch18_Link-Layer-Error-Detection-and-Multiple-Access/) | Link-layer services, parity checks, checksums, CRC, channel partitioning protocols, ALOHA, CSMA/CD, taking-turns protocols, DOCSIS | [Lecture notes](Ch18_Link-Layer-Error-Detection-and-Multiple-Access/Concepts_Lecture.md) |
| [Chapter 19 Link-Layer Addressing and ARP](Ch19_Link-Layer-Addressing-and-ARP/) | MAC addresses, static and dynamic mapping, ARP packets and operation, sending a datagram off the subnet, proxy ARP, the ARP package, RARP, ARP probes and ARP announcements, ARP security | [Lecture notes](Ch19_Link-Layer-Addressing-and-ARP/Concepts_Lecture.md) |
| [Chapter 20 Ethernet, Switches, and VLANs](Ch20_Ethernet-Switches-and-VLANs/) | IEEE 802 standards, the Ethernet frame, Ethernet evolution, repeaters, hubs, and bridges, switch self-learning, switches and routers, VLANs | [Lecture notes](Ch20_Ethernet-Switches-and-VLANs/Concepts_Lecture.md) |
| [Chapter 21 Wide Area Networks and Link Virtualization](Ch21_Wide-Area-Networks-and-Link-Virtualization/) | T lines, SONET, PPP, X.25, Frame Relay, ATM, MPLS, data center networks, a day in the life of a web page request | [Lecture notes](Ch21_Wide-Area-Networks-and-Link-Virtualization/Concepts_Lecture.md) |

## Part 7 Wireless and Mobile Networks

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 22 Wireless LANs and Bluetooth](Ch22_Wireless-LANs-and-Bluetooth/) | Wireless link characteristics, CDMA, IEEE 802.11 architecture, CSMA/CA and RTS/CTS, the 802.11 frame and addressing, hidden and exposed stations, rate adaptation and power management, Bluetooth, Zigbee | [Lecture notes](Ch22_Wireless-LANs-and-Bluetooth/Concepts_Lecture.md) |

## Supplementary Units

Units that supplement topics corresponding to no week of the [progress table](../Course-Information.md#5-weekly-plan-and-progress), following Computer Networking: A Top-Down Approach.

| Unit | Topics | Documents |
|:-----|:-----|:-----|
| [Chapter 23 P2P, Video Streaming, and Socket Programming](Ch23_P2P-Video-Streaming-and-Socket-Programming/) | P2P file distribution and BitTorrent, HTTP streaming and DASH, CDNs, UDP and TCP socket programming, the C socket interface | [Lecture notes](Ch23_P2P-Video-Streaming-and-Socket-Programming/Concepts_Lecture.md) |
| [Chapter 24 IPv6 and Generalized Forwarding](Ch24_IPv6-and-Generalized-Forwarding/) | IPv6 addresses, the IPv6 datagram and extension headers, transition from IPv4 to IPv6, ICMPv6, generalized forwarding and OpenFlow | [Lecture notes](Ch24_IPv6-and-Generalized-Forwarding/Concepts_Lecture.md) |
| [Chapter 25 Cellular Networks and Mobility](Ch25_Cellular-Networks-and-Mobility/) | Generations of cellular technology, 4G LTE, principles of mobility management, indirect and direct routing, Mobile IP, HLR and VLR, handoffs in GSM | [Lecture notes](Ch25_Cellular-Networks-and-Mobility/Concepts_Lecture.md) |
| [Chapter 26 Network Security](Ch26_Network-Security/) | Principles of cryptography, message integrity and digital signatures, end-point authentication, securing e-mail, TLS, IPsec and VPNs, tunneling, comparison of VPN protocols, wireless LAN security, firewalls and intrusion detection systems | [Lecture notes](Ch26_Network-Security/Concepts_Lecture.md) |
