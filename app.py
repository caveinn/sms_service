import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("getting")
        return json.dumps("trial")


Handler = MyHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        print("keyboard interupt")
        httpd.server_close()
