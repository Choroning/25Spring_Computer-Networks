"""
@file    http_server.py
@brief   Basic HTTP/1.1 server using Python sockets with multi-threaded
         connection handling. Supports GET and POST requests, static file
         serving, URL routing, and proper HTTP status codes.
@author  Cheolwon Park
@date    2025-06-15
"""

import json
import mimetypes
import os
import socket
import sys
import threading
from datetime import datetime

from http_parser import (
    HTTPRequest,
    HTTPResponse,
    build_error_response,
    parse_request,
)
from router import Router

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

HOST = "0.0.0.0"
PORT = 8080
BUFFER_SIZE = 4096
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")


# ---------------------------------------------------------------------------
# Request Handlers
# ---------------------------------------------------------------------------

def handle_index(request: HTTPRequest) -> HTTPResponse:
    """Serve the main index page."""
    return serve_static_file("/static/index.html")


def handle_echo(request: HTTPRequest) -> HTTPResponse:
    """Echo back the POST body as JSON."""
    response_data = {
        "status": "ok",
        "method": request.method,
        "path": request.path,
        "headers": request.headers,
        "body": request.body,
        "timestamp": datetime.now().isoformat(),
    }
    body = json.dumps(response_data, indent=2).encode("utf-8")
    response = HTTPResponse(200)
    response.set_body(body, "application/json; charset=utf-8")
    return response


def handle_hello(request: HTTPRequest) -> HTTPResponse:
    """Return a simple greeting with query parameter support."""
    name = request.query_params.get("name", "World")
    html = (
        f"<html><body>"
        f"<h1>Hello, {name}!</h1>"
        f"<p>You sent a {request.method} request to {request.path}.</p>"
        f"</body></html>"
    )
    response = HTTPResponse(200)
    response.set_body(html.encode("utf-8"), "text/html; charset=utf-8")
    return response


def handle_status(request: HTTPRequest) -> HTTPResponse:
    """Return server status as JSON."""
    data = {
        "server": "SimpleHTTP/1.0",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "python_version": sys.version,
    }
    body = json.dumps(data, indent=2).encode("utf-8")
    response = HTTPResponse(200)
    response.set_body(body, "application/json; charset=utf-8")
    return response


# ---------------------------------------------------------------------------
# Static File Serving
# ---------------------------------------------------------------------------

def serve_static_file(path: str) -> HTTPResponse:
    """
    Serve a static file from the STATIC_DIR directory.

    Args:
        path: URL path starting with /static/ (e.g., /static/index.html).

    Returns:
        HTTPResponse with file contents or a 404 error.
    """
    # Strip the /static/ prefix to get the relative file path
    relative_path = path.replace("/static/", "", 1)
    file_path = os.path.join(STATIC_DIR, relative_path)

    # Prevent directory traversal attacks
    file_path = os.path.realpath(file_path)
    if not file_path.startswith(os.path.realpath(STATIC_DIR)):
        return build_error_response(404, "File not found.")

    if not os.path.isfile(file_path):
        return build_error_response(404, f"File not found: {relative_path}")

    # Determine content type
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"

    try:
        with open(file_path, "rb") as f:
            content = f.read()
        response = HTTPResponse(200)
        response.set_body(content, content_type)
        return response
    except IOError:
        return build_error_response(500, "Error reading file.")


# ---------------------------------------------------------------------------
# Router Setup
# ---------------------------------------------------------------------------

def create_router() -> Router:
    """Create and configure the URL router with all application routes."""
    router = Router()

    # Page routes
    router.get("/", handle_index)
    router.get("/hello", handle_hello)

    # API routes
    router.get("/api/status", handle_status)
    router.post("/api/echo", handle_echo)

    return router


# ---------------------------------------------------------------------------
# Connection Handling
# ---------------------------------------------------------------------------

def handle_client(client_socket: socket.socket, client_addr: tuple,
                  router: Router) -> None:
    """
    Handle a single client connection in its own thread.

    Reads the raw HTTP request, parses it, routes it to the appropriate
    handler, and sends the response back to the client.

    Args:
        client_socket: The connected client socket.
        client_addr: Tuple of (host, port) for the client.
        router: The application router for dispatching requests.
    """
    try:
        # Receive data from the client
        raw_data = b""
        client_socket.settimeout(5.0)
        while True:
            try:
                chunk = client_socket.recv(BUFFER_SIZE)
                raw_data += chunk
                # If we received less than BUFFER_SIZE, we likely have the
                # full request (simple heuristic for this project)
                if len(chunk) < BUFFER_SIZE:
                    break
            except socket.timeout:
                break

        if not raw_data:
            return

        # Parse the HTTP request
        request = parse_request(raw_data)
        if request is None:
            response = build_error_response(400, "Malformed HTTP request.")
            client_socket.sendall(response.build())
            return

        # Log the request
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {client_addr[0]}:{client_addr[1]} "
              f"{request.method} {request.path}")

        # Handle static file requests
        if request.path.startswith("/static/"):
            if request.method == "GET":
                response = serve_static_file(request.path)
            else:
                response = build_error_response(405, "Method not allowed.")
        else:
            # Dispatch through the router
            response = router.dispatch(request)

        # Send the response
        client_socket.sendall(response.build())

    except Exception as e:
        print(f"[ERROR] Exception handling {client_addr}: {e}")
        try:
            error_response = build_error_response(
                500, "Internal server error."
            )
            client_socket.sendall(error_response.build())
        except Exception:
            pass

    finally:
        client_socket.close()


# ---------------------------------------------------------------------------
# Server Main Loop
# ---------------------------------------------------------------------------

def start_server(host: str = HOST, port: int = PORT) -> None:
    """
    Start the HTTP server and listen for incoming connections.

    Creates a TCP socket, binds to the specified host and port, and
    spawns a new thread for each incoming connection.

    Args:
        host: The hostname or IP address to bind to.
        port: The port number to listen on.
    """
    router = create_router()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"========================================")
    print(f"  Simple HTTP/1.1 Server")
    print(f"  Listening on http://{host}:{port}")
    print(f"  Static dir: {STATIC_DIR}")
    print(f"  Press Ctrl+C to stop")
    print(f"========================================")

    try:
        while True:
            client_socket, client_addr = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_addr, router),
                daemon=True,
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\n[INFO] Server shutting down...")

    finally:
        server_socket.close()
        print("[INFO] Server stopped.")


if __name__ == "__main__":
    # Allow port override via command-line argument
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}")
            sys.exit(1)

    start_server(port=port)
