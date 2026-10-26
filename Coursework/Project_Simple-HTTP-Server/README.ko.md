# 간단한 HTTP 서버

[레포지토리 안내](../../README.ko.md) | [English](README.md) | [한국어](README.ko.md)

> **최종 수정일:** 2026-10-26

---

## 개요

Python `socket` 모듈로 처음부터 구현한 기본 HTTP/1.1 서버이다. 이 프로젝트는 고수준 HTTP 라이브러리에 의존하지 않고 요청 파싱, 응답 생성, URL 라우팅, 정적 파일 제공을 구현하여 HTTP 프로토콜의 기초를 보여 준다.

## 기능

- **HTTP/1.1 프로토콜**: HTTP/1.1 명세에 따라 요청 줄(request line), 헤더, 본문을 파싱한다.
- **GET과 POST 지원**: 자원을 가져오는 GET 요청과 데이터를 제출하는 POST 요청을 처리한다.
- **정적 파일 제공**: `static/` 디렉터리의 HTML, CSS, JavaScript, 이미지 파일을 제공한다.
- **URL 라우팅**: 경로 매칭과 메서드 필터링을 지원하는 라우트 등록 기능을 제공한다.
- **멀티스레드**: 클라이언트 연결마다 스레드를 하나씩 만들어 요청을 동시에 처리한다.
- **상태 코드**: 상황에 맞는 HTTP 상태 코드(200, 404, 405, 500)를 반환한다.
- **보안**: 정적 파일 요청에서 디렉터리 순회(directory traversal)를 막는다.

## 프로젝트 구조

```text
Project_Simple-HTTP-Server/
├── http_server.py      # Main server: socket binding, threading, request dispatch
├── http_client.py      # Test client: send GET/POST requests, display responses
├── http_parser.py      # HTTP parsing: request/response objects, header parsing
├── router.py           # URL routing: path matching, handler registration
├── static/
│   ├── index.html      # Sample HTML page
│   └── style.css       # Sample CSS stylesheet
├── README.ko.md
└── README.md
```

## 사용법

### 서버 실행

```bash
# Start on default port 8080
python http_server.py

# Start on a custom port
python http_server.py 9000
```

### 클라이언트 사용

```bash
# Interactive mode
python http_client.py

# Interactive mode with custom host/port
python http_client.py 127.0.0.1 8080

# Run automated test suite
python http_client.py 127.0.0.1 8080 --test
```

### 클라이언트 명령 (대화형 모드)

```text
GET /                     # Fetch the index page
GET /hello?name=Alice     # Fetch greeting with query parameter
GET /api/status           # Get server status (JSON)
POST /api/echo message    # Echo back POST data (JSON)
test                      # Run all test cases
quit                      # Exit the client
```

## API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|---------------|------------------------------------|
| GET    | `/`           | 인덱스 페이지 제공 |
| GET    | `/hello`      | 인사 페이지 (`?name=` 지원) |
| GET    | `/api/status` | JSON 형식의 서버 상태 |
| POST   | `/api/echo`   | 요청 세부 정보를 JSON으로 에코 |
| GET    | `/static/*`   | 정적 파일 제공 |

## 동작 방식

1. **소켓 바인딩**: 서버가 TCP 소켓을 만들고 지정한 호스트와 포트에 바인딩한다.
2. **연결 수락**: 메인 루프가 들어오는 연결을 수락하고 연결마다 새 스레드를 만든다.
3. **요청 파싱**: 수신한 바이트를 메서드, 경로, 헤더, 본문으로 구성된 `HTTPRequest` 객체로 파싱한다.
4. **라우팅**: `Router`가 요청의 메서드와 경로에 맞는 등록된 핸들러 함수를 찾는다.
5. **응답 생성**: 핸들러가 반환한 `HTTPResponse` 객체를 올바른 HTTP 응답 바이트로 직렬화한다.
6. **정적 파일**: `/static/*` 요청은 MIME 타입을 판별하여 파일 시스템에서 바로 제공한다.

## 참고 문헌

- **Stanford CS144: Introduction to Computer Networking**, 네트워크 프로토콜과 HTTP 프로토콜, 소켓 프로그래밍의 기초 개념을 다룬다. 강의 자료는 [cs144.github.io](https://cs144.github.io/)에서 볼 수 있다.
- **CMU 15-441/641: Computer Networks**, 전송 프로토콜과 응용 계층 프로토콜, 네트워크 프로그래밍을 깊이 다룬다. 과목 페이지는 [computer-networks.cs.cmu.edu](https://computer-networks.cs.cmu.edu/)이다.
- **RFC 7230**: Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC 7231**: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content
- **Python `socket` 모듈 문서**: [docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)
