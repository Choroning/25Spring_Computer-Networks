"""
@file    http_client.py
@brief   Simple HTTP client for testing the HTTP server.
         Supports sending GET and POST requests and displaying responses.
@author  Cheolwon Park
@date    2025-06-15
"""

import json
import socket
import sys
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080
BUFFER_SIZE = 4096


# ---------------------------------------------------------------------------
# HTTP Client Functions
# ---------------------------------------------------------------------------

def send_request(host: str, port: int, method: str, path: str,
                 body: Optional[str] = None,
                 headers: Optional[dict] = None) -> str:
    """
    Send an HTTP request and return the raw response.

    Args:
        host: Server hostname or IP address.
        port: Server port number.
        method: HTTP method (GET or POST).
        path: Request path (e.g., /hello).
        body: Optional request body (for POST requests).
        headers: Optional dictionary of additional headers.

    Returns:
        Raw HTTP response as a string.
    """
    # Build the request
    request_line = f"{method.upper()} {path} HTTP/1.1\r\n"
    default_headers = {
        "Host": f"{host}:{port}",
        "User-Agent": "SimpleHTTPClient/1.0",
        "Accept": "*/*",
        "Connection": "close",
    }

    if headers:
        default_headers.update(headers)

    if body:
        default_headers["Content-Length"] = str(len(body.encode("utf-8")))
        if "Content-Type" not in default_headers:
            default_headers["Content-Type"] = "application/x-www-form-urlencoded"

    header_str = ""
    for key, value in default_headers.items():
        header_str += f"{key}: {value}\r\n"

    raw_request = request_line + header_str + "\r\n"
    if body:
        raw_request += body

    # Send via socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)

    try:
        sock.connect((host, port))
        sock.sendall(raw_request.encode("utf-8"))

        # Receive the response
        response = b""
        while True:
            try:
                chunk = sock.recv(BUFFER_SIZE)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                break

        return response.decode("utf-8", errors="replace")

    finally:
        sock.close()


def send_get(host: str, port: int, path: str) -> str:
    """Send a GET request."""
    return send_request(host, port, "GET", path)


def send_post(host: str, port: int, path: str, body: str,
              content_type: str = "application/x-www-form-urlencoded") -> str:
    """Send a POST request."""
    headers = {"Content-Type": content_type}
    return send_request(host, port, "POST", path, body=body, headers=headers)


# ---------------------------------------------------------------------------
# Response Display
# ---------------------------------------------------------------------------

def display_response(response: str) -> None:
    """
    Pretty-print an HTTP response, separating headers and body.

    Args:
        response: Raw HTTP response string.
    """
    if "\r\n\r\n" in response:
        headers, body = response.split("\r\n\r\n", 1)
    elif "\n\n" in response:
        headers, body = response.split("\n\n", 1)
    else:
        headers = response
        body = ""

    print("=" * 60)
    print("RESPONSE HEADERS:")
    print("-" * 60)
    print(headers)
    print("-" * 60)
    print("RESPONSE BODY:")
    print("-" * 60)

    # Attempt to pretty-print JSON bodies
    try:
        parsed = json.loads(body)
        print(json.dumps(parsed, indent=2))
    except (json.JSONDecodeError, ValueError):
        print(body[:2000] if len(body) > 2000 else body)

    print("=" * 60)


# ---------------------------------------------------------------------------
# Test Suite
# ---------------------------------------------------------------------------

def run_tests(host: str, port: int) -> None:
    """
    Run a suite of test requests against the server.

    Args:
        host: Server hostname.
        port: Server port.
    """
    print(f"\nTesting server at {host}:{port}\n")

    # Test 1: GET /
    print("[Test 1] GET /")
    resp = send_get(host, port, "/")
    display_response(resp)

    # Test 2: GET /hello
    print("\n[Test 2] GET /hello")
    resp = send_get(host, port, "/hello")
    display_response(resp)

    # Test 3: GET /hello?name=Student
    print("\n[Test 3] GET /hello?name=Student")
    resp = send_get(host, port, "/hello?name=Student")
    display_response(resp)

    # Test 4: GET /api/status
    print("\n[Test 4] GET /api/status")
    resp = send_get(host, port, "/api/status")
    display_response(resp)

    # Test 5: POST /api/echo
    print("\n[Test 5] POST /api/echo")
    resp = send_post(host, port, "/api/echo", "message=Hello+from+client")
    display_response(resp)

    # Test 6: POST /api/echo (JSON body)
    print("\n[Test 6] POST /api/echo (JSON)")
    json_body = json.dumps({"key": "value", "number": 42})
    resp = send_post(host, port, "/api/echo", json_body,
                     content_type="application/json")
    display_response(resp)

    # Test 7: GET /nonexistent (expect 404)
    print("\n[Test 7] GET /nonexistent (expect 404)")
    resp = send_get(host, port, "/nonexistent")
    display_response(resp)

    # Test 8: GET /static/style.css
    print("\n[Test 8] GET /static/style.css")
    resp = send_get(host, port, "/static/style.css")
    display_response(resp)

    print("\nAll tests completed.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    host = DEFAULT_HOST
    port = DEFAULT_PORT

    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print(f"Invalid port: {sys.argv[2]}")
            sys.exit(1)

    if len(sys.argv) > 3 and sys.argv[3] == "--test":
        run_tests(host, port)
    else:
        # Interactive mode
        print(f"HTTP Client - Target: {host}:{port}")
        print("Commands: GET <path> | POST <path> <body> | test | quit")
        print()

        while True:
            try:
                cmd = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye.")
                break

            if not cmd:
                continue
            if cmd.lower() == "quit":
                break
            if cmd.lower() == "test":
                run_tests(host, port)
                continue

            parts = cmd.split(maxsplit=2)
            method = parts[0].upper()

            if method == "GET" and len(parts) >= 2:
                resp = send_get(host, port, parts[1])
                display_response(resp)
            elif method == "POST" and len(parts) >= 3:
                resp = send_post(host, port, parts[1], parts[2])
                display_response(resp)
            elif method == "POST" and len(parts) == 2:
                resp = send_post(host, port, parts[1], "")
                display_response(resp)
            else:
                print("Usage: GET <path> | POST <path> [body] | test | quit")
