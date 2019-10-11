import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("getting")
        self.send_response(200, "OK")
        self.end_headers()
        response = json.dumps({"spample": "sample"})
        self.wfile.write(bytes(response, 'utf8'))



Handler = MyHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        print("keyboard interupt")
        httpd.server_close()
