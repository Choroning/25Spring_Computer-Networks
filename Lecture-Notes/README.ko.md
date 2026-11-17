# 강의 노트

[레포지토리 안내](../README.ko.md) | [English](README.md) | [한국어](README.ko.md)

> **최종 수정일:** 2026-11-18

각 부는 Computer Networking: A Top-Down Approach의 같은 번호의 장에 대응합니다.

## 1부 컴퓨터 네트워크와 인터넷

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [1장 컴퓨터 네트워크와 인터넷](Ch01_Computer-Networks-and-the-Internet/) | 인터넷의 구성 요소와 서비스, 프로토콜과 표준, 네트워크 가장자리와 접속 네트워크, 물리 매체, 패킷 교환과 회선 교환, 네트워크의 네트워크와 ISP 계층 구조, 지연, 손실, 처리량, 네트워크 공격, 인터넷의 역사 | [강의 노트](Ch01_Computer-Networks-and-the-Internet/Concepts_Lecture.ko.md) |
| [2장 프로토콜 계층과 네트워크 모델](Ch02_Protocol-Layers-and-Network-Models/) | 프로토콜 계층화, OSI 모델, TCP/IP 프로토콜 스위트, OSI 모델과 TCP/IP의 비교, 네 단계의 주소, 캡슐화와 역캡슐화, 다중화와 역다중화 | [강의 노트](Ch02_Protocol-Layers-and-Network-Models/Concepts_Lecture.ko.md) |

## 2부 응용 계층

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [3장 네트워크 응용과 웹](Ch03_Network-Applications-and-the-Web/) | 클라이언트-서버 구조와 P2P 구조, 프로세스와 소켓, 반복 서버와 동시 서버, 응용이 요구하는 전송 서비스, 웹 문서의 종류, HTTP 연결과 메시지 형식, 쿠키, 웹 캐싱과 조건부 GET, HTTP/2 | [강의 노트](Ch03_Network-Applications-and-the-Web/Concepts_Lecture.ko.md) |
| [4장 전자 메일, 원격 로그인, 파일 전송](Ch04_Electronic-Mail-Remote-Login-and-File-Transfer/) | 전자 메일의 구조, SMTP, SMTP와 HTTP의 비교, MIME, POP3와 IMAP, TELNET과 SSH, FTP와 TFTP | [강의 노트](Ch04_Electronic-Mail-Remote-Login-and-File-Transfer/Concepts_Lecture.ko.md) |
| [5장 도메인 이름 시스템 (DNS)](Ch05_Domain-Name-System/) | DNS의 서비스, 도메인 이름 공간, 계층적 DNS 서버와 영역, 재귀 질의와 반복 질의, DNS 캐싱, 자원 레코드와 DNS 메시지, 레코드의 등록과 DDNS, DNS 보안 | [강의 노트](Ch05_Domain-Name-System/Concepts_Lecture.ko.md) |

## 3부 전송 계층

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [6장 전송 계층 서비스와 UDP](Ch06_Transport-Layer-Services-and-UDP/) | 전송 계층의 역할, 프로세스 간 통신, 포트 번호와 소켓 주소, 다중화와 역다중화, 비연결형 서비스와 연결형 서비스, 사용자 데이터그램 형식, UDP 체크섬, UDP 응용, UDP 패키지 | [강의 노트](Ch06_Transport-Layer-Services-and-UDP/Concepts_Lecture.ko.md) |
| [7장 신뢰적 데이터 전송의 원리](Ch07_Principles-of-Reliable-Data-Transfer/) | 흐름 제어와 오류 제어, rdt 프로토콜, 정지 후 대기 프로토콜, 파이프라이닝, Go-Back-N, Selective Repeat, 순서 번호 공간과 윈도우 크기, 피기백 | [강의 노트](Ch07_Principles-of-Reliable-Data-Transfer/Concepts_Lecture.ko.md) |
| [8장 전송 제어 프로토콜 (TCP)](Ch08_Transmission-Control-Protocol/) | TCP 서비스, 번호 체계, 세그먼트 형식, 연결 설정과 해제, 상태 전이도, TCP의 윈도우, 흐름 제어, 오류 제어, RTT 추정과 타이머, 옵션, TCP 패키지 | [강의 노트](Ch08_Transmission-Control-Protocol/Concepts_Lecture.ko.md) |
| [9장 혼잡 제어](Ch09_Congestion-Control/) | 혼잡의 원인과 비용, 종단 간 혼잡 제어와 네트워크 지원 혼잡 제어, 개루프 혼잡 제어와 폐루프 혼잡 제어, 느린 시작, 혼잡 회피, 빠른 회복, AIMD와 TCP 처리량, 공정성, ECN | [강의 노트](Ch09_Congestion-Control/Concepts_Lecture.ko.md) |

## 4부 네트워크 계층: 데이터 평면

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [10장 네트워크 계층 개요](Ch10_Network-Layer-Overview/) | 포워딩과 라우팅, 데이터 평면과 제어 평면, 네트워크 서비스 모델, 데이터그램 방식과 가상 회선 방식, 네트워크 계층 서비스의 예, 네트워크 계층의 그 밖의 문제 | [강의 노트](Ch10_Network-Layer-Overview/Concepts_Lecture.ko.md) |
| [11장 인터넷 프로토콜 버전 4 (IPv4)](Ch11_Internet-Protocol-IPv4/) | IPv4 데이터그램 형식, 단편화와 재조립, 경로 MTU 발견, 옵션, 헤더 체크섬, IP의 보안, IP 패키지 | [강의 노트](Ch11_Internet-Protocol-IPv4/Concepts_Lecture.ko.md) |
| [12장 IPv4 주소](Ch12_IPv4-Addresses/) | 주소 표기법, 비트 단위 연산, 인터페이스와 서브넷, 클래스 기반 주소 지정, 클래스 없는 주소 지정(CIDR), 서브넷팅과 슈퍼넷팅, 주소 블록의 할당과 집약, 특수 주소, DHCP, NAT | [강의 노트](Ch12_IPv4-Addresses/Concepts_Lecture.ko.md) |
| [13장 전달, 포워딩, 라우터 구조](Ch13_Delivery-Forwarding-and-Router-Architecture/) | 직접 전달과 간접 전달, 포워딩 기법, 클래스 기반 포워딩과 클래스 없는 포워딩, 최장 접두사 일치, 주소 집약과 계층적 라우팅, 레이블 기반 포워딩과 MPLS, 라우터 구조, 패킷 스케줄링 | [강의 노트](Ch13_Delivery-Forwarding-and-Router-Architecture/Concepts_Lecture.ko.md) |

## 5부 네트워크 계층: 제어 평면

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [14장 라우팅 알고리즘](Ch14_Routing-Algorithms/) | 라우팅의 그래프 모델, 링크 상태 라우팅과 Dijkstra 알고리즘, 거리 벡터 라우팅과 Bellman-Ford 식, 무한 카운트 문제, 스플릿 호라이즌과 포이즌 리버스, 두 알고리즘의 비교 | [강의 노트](Ch14_Routing-Algorithms/Concepts_Lecture.ko.md) |
| [15장 인터넷 라우팅 프로토콜](Ch15_Internet-Routing-Protocols/) | 자율 시스템과 계층적 라우팅, RIP, OSPF, 경로 벡터 라우팅, BGP, IP 애니캐스트, SDN 제어 평면과 OpenFlow | [강의 노트](Ch15_Internet-Routing-Protocols/Concepts_Lecture.ko.md) |
| [16장 ICMPv4와 IGMP](Ch16_ICMPv4-and-IGMP/) | ICMP 메시지 형식, 오류 보고 메시지, 질의 메시지, ICMP 체크섬, ping과 traceroute, ICMP 패키지, ICMP와 보안, 멀티캐스트 주소, IGMP | [강의 노트](Ch16_ICMPv4-and-IGMP/Concepts_Lecture.ko.md) |
| [17장 네트워크 관리와 SNMP](Ch17_Network-Management-and-SNMP/) | 네트워크 관리의 구성 요소, 관리자와 에이전트, SMI와 BER 부호화, MIB, SNMP | [강의 노트](Ch17_Network-Management-and-SNMP/Concepts_Lecture.ko.md) |

## 6부 링크 계층과 LAN

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [18장 링크 계층, 오류 검출, 다중 접근](Ch18_Link-Layer-Error-Detection-and-Multiple-Access/) | 링크 계층 서비스, 패리티 검사, 체크섬, CRC, 채널 분할 프로토콜, ALOHA, CSMA/CD, 순번 프로토콜, DOCSIS | [강의 노트](Ch18_Link-Layer-Error-Detection-and-Multiple-Access/Concepts_Lecture.ko.md) |
| [19장 링크 계층 주소와 ARP](Ch19_Link-Layer-Addressing-and-ARP/) | MAC 주소, 정적 매핑과 동적 매핑, ARP 패킷과 동작, 서브넷 밖으로 데이터그램 보내기, 프록시 ARP, ARP 패키지, RARP, ARP 프로브와 ARP 알림, ARP 보안 | [강의 노트](Ch19_Link-Layer-Addressing-and-ARP/Concepts_Lecture.ko.md) |
| [20장 이더넷, 스위치, VLAN](Ch20_Ethernet-Switches-and-VLANs/) | IEEE 802 표준, 이더넷 프레임, 이더넷의 발전, 리피터, 허브, 브리지, 스위치의 자기 학습, 스위치와 라우터, VLAN | [강의 노트](Ch20_Ethernet-Switches-and-VLANs/Concepts_Lecture.ko.md) |
| [21장 광역 네트워크와 링크 가상화](Ch21_Wide-Area-Networks-and-Link-Virtualization/) | T 회선, SONET, PPP, X.25, 프레임 릴레이, ATM, MPLS, 데이터 센터 네트워크, 웹 페이지 요청의 전 과정 | [강의 노트](Ch21_Wide-Area-Networks-and-Link-Virtualization/Concepts_Lecture.ko.md) |

## 7부 무선 및 이동 네트워크

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [22장 무선 LAN과 블루투스](Ch22_Wireless-LANs-and-Bluetooth/) | 무선 링크의 특성, CDMA, IEEE 802.11 구조, CSMA/CA와 RTS/CTS, 802.11 프레임과 주소 지정, 숨은 스테이션과 노출 스테이션, 전송률 적응과 전력 관리, 블루투스, Zigbee | [강의 노트](Ch22_Wireless-LANs-and-Bluetooth/Concepts_Lecture.ko.md) |

## 보충 단원

[진도 표](../Course-Information.ko.md#5-주차별-계획-및-진도)의 어느 주차에도 대응하지 않는 주제를 Computer Networking: A Top-Down Approach를 따라 보충한 단원입니다.

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [23장 P2P, 비디오 스트리밍, 소켓 프로그래밍](Ch23_P2P-Video-Streaming-and-Socket-Programming/) | P2P 파일 배포와 BitTorrent, HTTP 스트리밍과 DASH, CDN, UDP 소켓 프로그래밍과 TCP 소켓 프로그래밍, C 소켓 인터페이스 | [강의 노트](Ch23_P2P-Video-Streaming-and-Socket-Programming/Concepts_Lecture.ko.md) |
| [24장 IPv6와 일반화된 포워딩](Ch24_IPv6-and-Generalized-Forwarding/) | IPv6 주소, IPv6 데이터그램과 확장 헤더, IPv4에서 IPv6로의 전환, ICMPv6, 일반화된 포워딩과 OpenFlow | [강의 노트](Ch24_IPv6-and-Generalized-Forwarding/Concepts_Lecture.ko.md) |
| [25장 셀룰러 네트워크와 이동성](Ch25_Cellular-Networks-and-Mobility/) | 셀룰러 기술의 세대, 4G LTE, 이동성 관리의 원리, 간접 라우팅과 직접 라우팅, 모바일 IP, HLR과 VLR, GSM의 핸드오프 | [강의 노트](Ch25_Cellular-Networks-and-Mobility/Concepts_Lecture.ko.md) |
| [26장 네트워크 보안](Ch26_Network-Security/) | 암호화의 원리, 메시지 무결성과 전자 서명, 종단점 인증, 전자 메일 보안, TLS, IPsec과 VPN, 터널링, VPN 프로토콜의 비교, 무선 LAN 보안, 방화벽과 침입 탐지 시스템 | [강의 노트](Ch26_Network-Security/Concepts_Lecture.ko.md) |
