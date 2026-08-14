from http.server import HTTPServer, BaseHTTPRequestHandler

class Router(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("Hello, Welcome to the home page!", "utf-8"))
        
def main():
    address = ("localhost", 8080)
    server = HTTPServer(address, Router)
    try:
        print("Starting")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped")
        sever.server_close()
if __name__ == "__main__":
    main()
