"""
@file    router.py
@brief   URL routing with path matching and handler registration
@author  Cheolwon Park
@date    2025-06-15
"""

from typing import Callable, Dict, List, Optional, Tuple
from http_parser import HTTPRequest, HTTPResponse, build_error_response


# Handler type: takes an HTTPRequest and returns an HTTPResponse
Handler = Callable[[HTTPRequest], HTTPResponse]


class Route:
    """Represents a single route with a method, path pattern, and handler."""

    def __init__(self, method: str, path: str, handler: Handler):
        self.method = method.upper()
        self.path = path
        self.handler = handler

    def matches(self, method: str, path: str) -> bool:
        """
        Check if this route matches the given method and path.

        Args:
            method: HTTP method (GET, POST, etc.).
            path: Request path to match against.

        Returns:
            True if the route matches, False otherwise.
        """
        return self.method == method.upper() and self._match_path(path)

    def _match_path(self, path: str) -> bool:
        """
        Match the request path against this route's pattern.

        Supports exact matching and simple wildcard segments using '*'.

        Args:
            path: Request path to match.

        Returns:
            True if the path matches the pattern.
        """
        # Normalize trailing slashes
        pattern = self.path.rstrip("/") or "/"
        target = path.rstrip("/") or "/"

        # Exact match
        if pattern == target:
            return True

        # Simple wildcard matching (e.g., "/api/*")
        if pattern.endswith("/*"):
            prefix = pattern[:-2]
            return target.startswith(prefix)

        return False


class Router:
    """
    URL router that maps HTTP method + path combinations to handler functions.

    Usage:
        router = Router()
        router.add_route("GET", "/", index_handler)
        router.add_route("POST", "/api/data", data_handler)
        response = router.dispatch(request)
    """

    def __init__(self):
        self._routes: List[Route] = []

    def add_route(self, method: str, path: str, handler: Handler) -> None:
        """
        Register a handler for a specific HTTP method and path.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.).
            path: URL path pattern to match.
            handler: Callable that takes an HTTPRequest and returns an HTTPResponse.
        """
        route = Route(method, path, handler)
        self._routes.append(route)

    def get(self, path: str, handler: Handler) -> None:
        """Shortcut to register a GET route."""
        self.add_route("GET", path, handler)

    def post(self, path: str, handler: Handler) -> None:
        """Shortcut to register a POST route."""
        self.add_route("POST", path, handler)

    def dispatch(self, request: HTTPRequest) -> HTTPResponse:
        """
        Find a matching route and invoke its handler.

        If a matching path is found but the method does not match,
        returns 405 Method Not Allowed. If no path matches, returns
        404 Not Found.

        Args:
            request: Parsed HTTPRequest object.

        Returns:
            HTTPResponse from the matched handler or an error response.
        """
        path_matched = False

        for route in self._routes:
            if route._match_path(request.path):
                path_matched = True
                if route.method == request.method:
                    return route.handler(request)

        if path_matched:
            return build_error_response(
                405, f"Method {request.method} is not allowed for {request.path}."
            )

        return build_error_response(
            404, f"The requested URL {request.path} was not found on this server."
        )
