"""
@file    http_parser.py
@brief   Parse HTTP request lines, headers, body; build HTTP responses
@author  Cheolwon Park
@date    2025-06-15
"""

from typing import Dict, Optional, Tuple


class HTTPRequest:
    """Parsed HTTP request object."""

    def __init__(self):
        self.method: str = ""
        self.path: str = ""
        self.version: str = "HTTP/1.1"
        self.headers: Dict[str, str] = {}
        self.body: str = ""
        self.query_params: Dict[str, str] = {}


class HTTPResponse:
    """HTTP response builder."""

    STATUS_MESSAGES = {
        200: "OK",
        201: "Created",
        301: "Moved Permanently",
        302: "Found",
        304: "Not Modified",
        400: "Bad Request",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }

    def __init__(self, status_code: int = 200):
        self.status_code: int = status_code
        self.headers: Dict[str, str] = {
            "Server": "SimpleHTTP/1.0",
            "Connection": "close",
        }
        self.body: bytes = b""

    def set_header(self, key: str, value: str) -> "HTTPResponse":
        """Set a response header."""
        self.headers[key] = value
        return self

    def set_body(self, body: bytes, content_type: str = "text/html") -> "HTTPResponse":
        """Set the response body and Content-Type header."""
        self.body = body
        self.headers["Content-Type"] = content_type
        self.headers["Content-Length"] = str(len(body))
        return self

    def build(self) -> bytes:
        """Build the raw HTTP response bytes."""
        status_msg = self.STATUS_MESSAGES.get(self.status_code, "Unknown")
        status_line = f"HTTP/1.1 {self.status_code} {status_msg}\r\n"

        header_lines = ""
        for key, value in self.headers.items():
            header_lines += f"{key}: {value}\r\n"

        response = (status_line + header_lines + "\r\n").encode("utf-8")
        response += self.body
        return response


def parse_request(raw_data: bytes) -> Optional[HTTPRequest]:
    """
    Parse raw HTTP request bytes into an HTTPRequest object.

    Args:
        raw_data: Raw bytes received from the client socket.

    Returns:
        HTTPRequest object if parsing succeeds, None otherwise.
    """
    try:
        text = raw_data.decode("utf-8", errors="replace")

        # Split headers and body
        if "\r\n\r\n" in text:
            header_section, body = text.split("\r\n\r\n", 1)
        elif "\n\n" in text:
            header_section, body = text.split("\n\n", 1)
        else:
            header_section = text
            body = ""

        lines = header_section.split("\r\n")
        if not lines:
            lines = header_section.split("\n")

        # Parse request line: METHOD PATH VERSION
        request_line = lines[0]
        parts = request_line.split(" ")
        if len(parts) < 2:
            return None

        request = HTTPRequest()
        request.method = parts[0].upper()
        request.version = parts[2] if len(parts) > 2 else "HTTP/1.1"

        # Parse path and query string
        full_path = parts[1]
        if "?" in full_path:
            request.path, query_string = full_path.split("?", 1)
            request.query_params = _parse_query_string(query_string)
        else:
            request.path = full_path

        # Parse headers
        for line in lines[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                request.headers[key.strip()] = value.strip()

        # Honor Content-Length: truncate body if the header is present
        cl = request.headers.get("Content-Length")
        if cl is not None:
            try:
                body = body[:int(cl)]
            except ValueError:
                pass

        request.body = body
        return request

    except Exception:
        return None


def _parse_query_string(query_string: str) -> Dict[str, str]:
    """
    Parse a URL query string into a dictionary.

    Args:
        query_string: The query string portion of a URL (e.g., "key1=val1&key2=val2").

    Returns:
        Dictionary of query parameter key-value pairs.
    """
    params = {}
    if not query_string:
        return params
    for pair in query_string.split("&"):
        if "=" in pair:
            key, value = pair.split("=", 1)
            params[key] = value
        else:
            params[pair] = ""
    return params


def build_error_response(status_code: int, message: str = "") -> HTTPResponse:
    """
    Build an HTTP error response with an HTML body.

    Args:
        status_code: HTTP status code (e.g., 404, 405, 500).
        message: Optional custom error message.

    Returns:
        HTTPResponse object ready to be sent.
    """
    status_msg = HTTPResponse.STATUS_MESSAGES.get(status_code, "Unknown Error")
    if not message:
        message = status_msg

    html = (
        f"<html><head><title>{status_code} {status_msg}</title></head>"
        f"<body><h1>{status_code} {status_msg}</h1>"
        f"<p>{message}</p></body></html>"
    )

    response = HTTPResponse(status_code)
    response.set_body(html.encode("utf-8"), "text/html; charset=utf-8")
    return response
