from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b"Hello from Effective Mobile!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()
