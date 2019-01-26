#import modules to get filepath, to open browser, opening url
import os, webbrowser, urllib.request

#creating vars to store local file name and url
url = "http://evtgit01.evtcorp.com/yrutenberg/Tech-Challenge/raw/master/evt-web.html"
file = "index.html"

#translating url into text
webpage = urllib.request.urlopen(url)
html = webpage.read()
print(html)

#writing text to index.html file
with open(file, "wb") as text_file:
	text_file.write(html)

#auto open default browser to index.html
<<<<<<< HEAD
webbrowser.open_new_tab("file://" + os.path.realpath(file))

#specifying local port number
PORT = 8000

#create the request handler
reqHandler = http.server.SimpleHTTPRequestHandler

#create the TCP server and pass in port and reqHandler
#returns the active port and begins running server, active on any IP
with socketserver.TCPServer(("", PORT), reqHandler) as httpd:
	print("Active at port", PORT)
	httpd.serve_forever()
=======
webbrowser.open_new_tab("192.168.99.100:80")
>>>>>>> 9cd44d234d303c8780591830ae2f6640082eec5c
