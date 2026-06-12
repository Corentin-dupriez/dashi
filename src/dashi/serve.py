import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000


def serve() -> None:
    handler = http.server.SimpleHTTPRequestHandler

    os.chdir(Path.cwd() / "builds")

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving on http://localhost:{PORT}")
        httpd.serve_forever()
