import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

#with socketserver.TCPServer(("", PORT), Handler) as httpd:
httpd = socketserver.TCPServer(("",PORT),Handler)
print("serving at port", PORT)
httpd.serve_forever()
