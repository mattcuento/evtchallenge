#import modules to get filepath, to open browser, opening url
import os, webbrowser, urllib.request

#creating vars to store local file name and url
url = "http://evtgit01.evtcorp.com/yrutenberg/Tech-Challenge/raw/master/evt-web.html"
file = "index.html"

#translating url into text
webpage = urllib.request.urlopen(url)
html = webpage.read()

#writing text to index.html file
with open(file, "wb") as text_file:
	text_file.write(html)

#auto open default browser to index.html
webbrowser.open_new_tab("192.168.99.100:80")
