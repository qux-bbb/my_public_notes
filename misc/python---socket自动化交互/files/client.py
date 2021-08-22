# coding:utf8
# python3

import sys
import re
import socket
from threading import Thread


class SocketInteraction:
    tcp_socket = None

    def __init__(self, host, port):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.connect((host, port))

    def __del__(self):
        self.tcp_socket.close()

    def recvline(self):
        return self.recvuntil('\n')
    
    def recv_n(self, n):
        return self.tcp_socket.recv(n).decode('utf8')

    def recvuntil(self, want_end_str):
        current_str = ''
        while True:
            current_str += self.recv_n(1)
            if current_str.endswith(want_end_str):
                return current_str

    def recvuntil_re(self, want_re_str):
        current_str = ''
        while True:
            current_str += self.recv_n(1)
            s = re.search(want_re_str, current_str)
            if s:
                return [current_str, s]

    def send(self, send_str):
        final_bytes = send_str.encode('utf8')
        self.tcp_socket.send(final_bytes)

    def sendline(self, send_str):
        self.send(send_str+'\n')
    
    def interact(self):
        def recv_loop():
            while True:
                c = self.recv_n(1)
                # print 写到控制台会有延时，直接用系统io写
                sys.stdout.write(c)
                sys.stdout.flush()

        def send_loop():
            while True:
                send_str = input()
                self.sendline(send_str)

        recv_thread = Thread(target=recv_loop)
        send_thread = Thread(target=send_loop)

        recv_thread.start()
        send_thread.start()

        recv_thread.join()
        send_thread.join()



si = SocketInteraction('127.0.0.1', 9999)
for i in range(2):
    content = si.recvuntil_re(r'input (\d+): ')
    print(content[0])
    num = content[1].group(1)
    print(repr(num))
    si.sendline(num)
content = si.recvline()
print(content)
