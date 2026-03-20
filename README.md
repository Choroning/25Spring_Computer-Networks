# [Spring 2025] Computer Networks

![Last Commit](https://img.shields.io/github/last-commit/Choroning/25Spring_Computer-Networks)
![Languages](https://img.shields.io/github/languages/top/Choroning/25Spring_Computer-Networks)

This repository organizes and stores networking concepts and protocol analyses written for university lectures and assignments.

*Author: Cheolwon Park (Korea University Sejong, CSE) – Year 2 (Sophomore) as of 2025*
<br><br>

## 📑 Table of Contents

- [About This Repository](#about-this-repository)
- [Course Information](#course-information)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [License](#license)

---


<br><a name="about-this-repository"></a>
## 📝 About This Repository

This repository contains materials and implementations developed for a university-level Computer Networks course, including:

- **Concepts.md** files for each chapter with comprehensive explanations of networking protocols and theories
- Lecture notes, protocol analyses, and student presentation materials (DHCP, NAT, ARP, DNS, VPN, Tunneling)
- Improved Python code files with **Doxygen-style headers** documenting purpose, usage, and structure
- A **term project** (Simple HTTP Server) designed with references to CS curricula at top universities

The course covers the TCP/IP protocol suite from the data link layer through the application layer, including IP addressing, routing, transport protocols, and network security.

<br><a name="course-information"></a>
## 📚 Course Information

- **Semester:** Spring 2025 (March - June)
- **Affiliation:** Korea University Sejong

| Course&nbsp;Code| Course            | Type          | Instructor      | Department                              |
|:----------:|:------------------|:-------------:|:---------------:|:----------------------------------------|
|`DCCS307-01`|COMPUTER NETWORKS|Major Required|Prof. Seungyeon&nbsp;Kim|Department of Computer Convergence Software|

- **📖 References**

| Type | Contents |
|:----:|:---------|
|Textbook|"TCP/IP Protocol Suite, 4th Edition" by Behrouz A. Forouzan (McGraw-Hill)|
|Reference|"Computer Networking: A Top-Down Approach, 7th Edition" by Kurose and Ross|
|Lecture Notes|Slides and handwritten notes provided by instructor|

<br><a name="prerequisites"></a>
## ✅ Prerequisites

- Interest in computer networking and communication protocols

- **💻 Development Environment**

| Tool | Company |  OS  | Notes |
|:-----|:-------:|:----:|:------|
|Wireshark|Wireshark Foundation|macOS|packet analysis|
|Visual Studio Code|Microsoft|macOS|    |

<br><a name="repository-structure"></a>
## 🗂 Repository Structure

```plaintext
25Spring_Computer-Networks
├── Chapter01-02_Introduction-and-Network-Layer
│   └── Concepts.md
├── Chapter03_Underlying-Technology
│   └── Concepts.md
├── Chapter04_Introduction-to-Network-Layer
│   └── Concepts.md
├── Chapter05_IPv4-Addresses
│   └── Concepts.md
├── Chapter06_Delivery-and-Forwarding
│   └── Concepts.md
├── Chapter07_Internet-Protocol-IPv4
│   └── Concepts.md
├── Chapter08_ARP
│   └── Concepts.md
├── Chapter09_ICMPv4
│   └── Concepts.md
├── Chapter13_Introduction-to-Transport-Layer
│   └── Concepts.md
├── Chapter14_UDP
│   └── Concepts.md
├── Chapter15_TCP
│   └── Concepts.md
├── Project_Simple-HTTP-Server
│   ├── static
│   │   ├── index.html
│   │   └── style.css
│   ├── http_client.py
│   ├── http_parser.py
│   ├── http_server.py
│   ├── README.md
│   └── router.py
├── LICENSE
├── README.ko.md
└── README.md

13 directories, 20 files
```

<br><a name="license"></a>
## 🤝 License

This repository is released under the [Apache License 2.0](LICENSE).

---
