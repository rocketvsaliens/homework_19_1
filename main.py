from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostname = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    @staticmethod
    def __get_html_content():
        with open('index.html', encoding='utf-8') as index:
            return index.read()

    def do_GET(self):
        parse_qs(urlparse(self.path).query)
        page = self.__get_html_content()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == '__main__':
    web_server = HTTPServer((hostname, server_port), MyServer)
    print('Server started http://%s:%s' % (hostname, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')
