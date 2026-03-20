# Project: Simple HTTP Server

> **Last Updated:** 2025-06-15

---

## Overview

A basic HTTP/1.1 server built from scratch using Python's `socket` module. This project demonstrates the fundamentals of the HTTP protocol by implementing request parsing, response building, URL routing, and static file serving without relying on high-level HTTP libraries.

## Features

- **HTTP/1.1 Protocol**: Parses request lines, headers, and bodies according to HTTP/1.1 specifications
- **GET & POST Support**: Handles GET requests for resource retrieval and POST requests for data submission
- **Static File Serving**: Serves HTML, CSS, JavaScript, and image files from the `static/` directory
- **URL Routing**: Configurable route registration with path matching and method filtering
- **Multi-threaded**: Spawns one thread per client connection for concurrent request handling
- **Status Codes**: Returns appropriate HTTP status codes (200, 404, 405, 500)
- **Security**: Directory traversal prevention for static file requests

## Project Structure

```
Project_Simple-HTTP-Server/
├── http_server.py      # Main server: socket binding, threading, request dispatch
├── http_client.py      # Test client: send GET/POST requests, display responses
├── http_parser.py      # HTTP parsing: request/response objects, header parsing
├── router.py           # URL routing: path matching, handler registration
├── static/
│   ├── index.html      # Sample HTML page
│   └── style.css       # Sample CSS stylesheet
└── README.md
```

## Usage

### Starting the Server

```bash
# Start on default port 8080
python http_server.py

# Start on a custom port
python http_server.py 9000
```

### Using the Client

```bash
# Interactive mode
python http_client.py

# Interactive mode with custom host/port
python http_client.py 127.0.0.1 8080

# Run automated test suite
python http_client.py 127.0.0.1 8080 --test
```

### Client Commands (Interactive Mode)

```
GET /                     # Fetch the index page
GET /hello?name=Alice     # Fetch greeting with query parameter
GET /api/status           # Get server status (JSON)
POST /api/echo message    # Echo back POST data (JSON)
test                      # Run all test cases
quit                      # Exit the client
```

## API Endpoints

| Method | Path          | Description                        |
|--------|---------------|------------------------------------|
| GET    | `/`           | Serve the index page               |
| GET    | `/hello`      | Greeting page (supports `?name=`)  |
| GET    | `/api/status` | Server status as JSON              |
| POST   | `/api/echo`   | Echo request details as JSON       |
| GET    | `/static/*`   | Serve static files                 |

## How It Works

1. **Socket Binding**: The server creates a TCP socket and binds to the specified host and port
2. **Connection Acceptance**: The main loop accepts incoming connections and spawns a new thread for each
3. **Request Parsing**: Raw bytes are parsed into structured `HTTPRequest` objects (method, path, headers, body)
4. **Routing**: The `Router` matches the request method and path to a registered handler function
5. **Response Building**: Handlers return `HTTPResponse` objects that are serialized into valid HTTP response bytes
6. **Static Files**: Requests to `/static/*` are served directly from the filesystem with MIME type detection

## References

- **Stanford CS144: Introduction to Computer Networking** - Foundational concepts on network protocols, the HTTP protocol, and socket programming. Course materials available at [cs144.github.io](https://cs144.github.io/).
- **CMU 15-441/641: Computer Networks** - In-depth coverage of transport protocols, application-layer protocols, and network programming. Course page at [computer-networks.cs.cmu.edu](https://computer-networks.cs.cmu.edu/).
- **RFC 7230**: Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- **RFC 7231**: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content
- **Python `socket` Module Documentation**: [docs.python.org/3/library/socket.html](https://docs.python.org/3/library/socket.html)
