import http.server, socketserver

#specifying local port number
PORT = 8000

#create the request handler
reqHandler = http.server.SimpleHTTPRequestHandler

#create the TCP server and pass in port and reqHandler
returns the active port and begins running server, active on any IP
with socketserver.TCPServer(("0.0.0.0", PORT), reqHandler) as httpd:
	print("Active at port", PORT)
	httpd.serve_forever()
