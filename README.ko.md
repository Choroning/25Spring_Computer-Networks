# [2025학년도 봄학기] 컴퓨터네트워크

![Last Commit](https://img.shields.io/github/last-commit/Choroning/25Spring_Computer-Networks)
![Languages](https://img.shields.io/github/languages/top/Choroning/25Spring_Computer-Networks)

이 레포지토리는 대학 강의 및 과제를 위해 작성된 네트워크 개념 및 프로토콜 분석 자료를 체계적으로 정리하고 보관합니다.

*작성자: 박철원 (고려대학교(세종), 컴퓨터융합소프트웨어학과) - 2025년 기준 2학년*
<br><br>

## 📑 목차

- [레포지토리 소개](#about-this-repository)
- [강의 정보](#course-information)
- [사전 요구사항](#prerequisites)
- [레포지토리 구조](#repository-structure)
- [라이선스](#license)

---


<br><a name="about-this-repository"></a>
## 📝 레포지토리 소개

이 레포지토리에는 대학 수준의 컴퓨터네트워크 과목을 위해 작성된 자료가 포함되어 있습니다:

- 각 챕터별 네트워크 프로토콜 및 이론을 종합적으로 정리한 **Concepts.md** 파일
- 강의 노트, 프로토콜 분석, 학생 발표 자료 (DHCP, NAT, ARP, DNS, VPN, Tunneling)
- 목적, 사용법, 구조를 문서화한 **Doxygen 스타일 헤더**가 포함된 개선된 Python 코드 파일
- 해외 CS 명문 대학 커리큘럼을 참고하여 설계한 **텀 프로젝트** (Simple HTTP Server)

본 과목은 데이터 링크 계층부터 응용 계층까지 TCP/IP 프로토콜 스위트를 다루며, IP 주소 체계, 라우팅, 전송 프로토콜, 네트워크 보안을 포함합니다.

<br><a name="course-information"></a>
## 📚 강의 정보

- **학기:** 2025학년도 봄학기 (3월 - 6월)
- **소속:** 고려대학교(세종)

|학수번호      |강의명    |이수구분|교수자|개설학과|
|:----------:|:-------|:----:|:------:|:----------------|
|`DCCS307-01`|컴퓨터네트워크|전공필수|김승연 교수|컴퓨터융합소프트웨어학과|

- **📖 참고 자료**

| 유형 | 내용 |
|:----:|:---------|
|교재|"TCP/IP Protocol Suite, 4th Edition" by Behrouz A. Forouzan (McGraw-Hill)|
|참고도서|"Computer Networking: A Top-Down Approach, 7th Edition" by Kurose and Ross|
|강의자료|교수자 제공 슬라이드 및 필기 노트|

<br><a name="prerequisites"></a>
## ✅ 사전 요구사항

- 컴퓨터 네트워크 및 통신 프로토콜에 대한 관심

- **💻 개발 환경**

| 도구 | 회사 |  운영체제  | 비고 |
|:-----|:-------:|:----:|:------|
|Wireshark|Wireshark Foundation|macOS|패킷 분석|
|Visual Studio Code|Microsoft|macOS|    |

<br><a name="repository-structure"></a>
## 🗂 레포지토리 구조

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

13개의 디렉토리, 20개의 파일
```

<br><a name="license"></a>
## 🤝 라이선스

이 레포지토리는 [Apache License 2.0](LICENSE) 하에 배포됩니다.

---
