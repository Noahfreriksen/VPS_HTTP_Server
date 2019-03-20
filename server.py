import http.server
import socketserver

PORT = 8081
# Handler = http.server.SimpleHTTPRequestHandler


class Handler(http.server.BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(1)
        return


# with socketserver.TCPServer(("", PORT), Handler) as httpd:
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

KeyboardInterrupt:
print 'stopped'
httpd.socket.close()

