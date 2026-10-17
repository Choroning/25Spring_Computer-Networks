# [2025학년도 봄학기] 컴퓨터네트워크

![Last Commit](https://img.shields.io/github/last-commit/Choroning/25Spring_Computer-Networks)
![Languages](https://img.shields.io/github/languages/top/Choroning/25Spring_Computer-Networks)

이 레포지토리는 컴퓨터네트워크 과목의 이중 언어 강의 노트와 수업 결과물을 정리한 아카이브입니다.

*작성자: 박철원 (고려대학교(세종), 컴퓨터소프트웨어학과) - 2025년 기준 2학년*
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

이 레포지토리에는 TCP/IP 프로토콜 스위트를 다루는 컴퓨터네트워크 과목의 강의 노트와 프로젝트가 담겨 있습니다.

- `Lecture-Notes/`에는 교재의 장마다 개념과 원리를 정리한 강의 노트가 있습니다. 강의자료가 교재의 장 단위로 구성되어 있어 단원도 장 번호(`Ch##`)로 나눴습니다.
- 모든 강의 노트는 영어 파일(`.md`)과 한국어 파일(`.ko.md`)이 같은 구성으로 짝을 이룹니다.
- `Coursework/`에는 텀 프로젝트인 Simple HTTP Server의 코드가 있습니다.

> **🤖 AI 에이전트 활용**
> 강의 노트의 정리와 번역, 레포지토리 구조 정리에 [Claude Code](https://claude.ai/download)를 활용했습니다.

<br><a name="course-information"></a>
## 📚 강의 정보

- **학기:** 2025학년도 봄학기 (3월 - 6월)
- **소속:** 고려대학교(세종)

|학수번호      |강의명    |이수구분|교수자|개설학과|
|:----------:|:-------|:----:|:------:|:----------------|
|`DCCS307-01`|컴퓨터네트워크|전공필수|김승연 교수|컴퓨터소프트웨어학과|

### 과목 개요

네트워크 소프트웨어와 하드웨어를 다루는 전공필수 과목으로, Forouzan의 교재를 따라 TCP/IP 프로토콜 스위트의 구조를 공부한다. 인터넷과 네트워크 모델, 기반 기술, IPv4 주소 체계와 전달, ARP와 ICMP, 전송 계층의 UDP와 TCP를 다루며, 강의계획서는 라우팅 프로토콜과 응용 계층(DNS, TELNET, FTP, SMTP, HTTP)까지 계획했다. 교수자, 수업 일정과 형식, 평가, 주차별 계획 및 진도, 참고 자료는 [강의 정보 문서](Course-Information.ko.md)에 정리했다.

<br><a name="prerequisites"></a>
## ✅ 사전 요구사항

- 지정된 선수 과목은 없습니다.
- 컴퓨터 네트워크와 통신 프로토콜에 관심이 있으면 충분합니다.

- **💻 개발 환경**

| 도구 | 회사 |  운영체제  | 비고 |
|:-----|:-------:|:----:|:------|
|Wireshark|Wireshark Foundation|macOS|패킷 분석|
|Visual Studio Code|Microsoft|macOS|    |

<br><a name="repository-structure"></a>
## 🗂 레포지토리 구조

```plaintext
25Spring_Computer-Networks
├── Lecture-Notes               교재 장별 강의 노트
├── Coursework                  텀 프로젝트
├── Course-Information.ko.md    수업 운영 정보
├── Course-Information.md
├── LICENSE                     문서 라이선스 (CC BY-NC-SA 4.0)
├── LICENSE-CODE                코드 라이선스 (PolyForm Noncommercial 1.0.0)
├── README.ko.md
└── README.md
```

단원 목록은 [`Lecture-Notes` 색인](Lecture-Notes/README.ko.md)에, 프로젝트는 [`Coursework` 색인](Coursework/README.ko.md)에 있습니다.

<br><a name="license"></a>
## 🤝 라이선스

이 레포지토리의 문서(강의 노트, 해설, 요약지)는 [CC BY-NC-SA 4.0](LICENSE), 코드는 [PolyForm Noncommercial 1.0.0](LICENSE-CODE)에 따라 배포됩니다. 강의자료와 교재에서 가져온 그림과 예제 코드, 강의가 배포한 과제 원본과 템플릿 코드는 원저작자에게 권리가 있으며 이 라이선스의 대상이 아닙니다.

---
