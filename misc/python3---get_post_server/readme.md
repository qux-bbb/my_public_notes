# python3---get_post_server

keywords: http请求 http响应  

接收任意get、post请求。  

```python
# coding:utf8

"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print('=={:=<80}'.format('begin'))
        print('GET request,')
        print('Path: {}'.format(self.path))
        print('Headers:')
        print(self.headers)
        self._set_response()
        self.wfile.write('GET request for {}'.format(self.path).encode('utf-8'))
        print('=={:=<80}'.format('end'))
        print()

    def do_POST(self):
        print('=={:=<80}'.format('begin'))
        content_length = int(self.headers.get('Content-Length', '0')) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        want_len = 300
        if len(post_data) > want_len:
            print_data = post_data[:want_len]
        else:
            print_data = post_data
        print('POST request,')
        print('Path: {}'.format(self.path))
        print('Headers:')
        print(self.headers)
        print('Body(part):')
        try:
            print(print_data.decode('utf8'))
        except:
            print(print_data)
        print()
        print()

        self._set_response()
        self.wfile.write('POST request for {}'.format(self.path).encode('utf-8'))
        print('=={:=<80}'.format('end'))
        print()

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd... port: {}'.format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd.')

if __name__ == '__main__':
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
```


原链接: https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7  


---
2021/10/14  
