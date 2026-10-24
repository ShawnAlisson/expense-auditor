"""Serve the UI and proxy /api/verify to the Sapling endpoint. `python3 server.py` -> :8000"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from sapling import verify


class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = {"/": "web/index.html", "/report.json": "data/report.json", "/results.json": "data/results.json"}.get(self.path.split("?")[0])
        if not path or not os.path.exists(path):
            return self._send(404, b"{}")
        ctype = "text/html; charset=utf-8" if path.endswith(".html") else "application/json"
        self._send(200, open(path, "rb").read(), ctype)

    def do_POST(self):
        if self.path != "/api/verify":
            return self._send(404, b"{}")
        d = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        try:
            out = verify(d["policy"], d["evidence"], d["claim"])
        except Exception as e:  # surface upstream errors to the UI
            return self._send(502, json.dumps({"error": str(e)}).encode())
        self._send(200, json.dumps(out).encode())

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"http://localhost:{port}")
    ThreadingHTTPServer(("", port), H).serve_forever()
