import http.server
import socketserver
import cgi

PORT = 8081
# Handler = http.server.SimpleHTTPRequestHandler


class Handler(http.server.BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(bytes("1", 'UTF-8'))
        return

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        print(self.headers)
        post_body = self.rfile.read(1)
        print(post_body)
        return
try:
    # with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

except KeyboardInterrupt:
    print('stopped')
    httpd.socket.close()

