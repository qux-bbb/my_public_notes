# coding:utf-8
# python3

import sys
import re
import subprocess
from threading import Thread


class ProcessInteraction:
    process = None

    def __init__(self, command):
        self.process = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def __del__(self):
        self.process.stdin.close()
        self.process.stdout.close()

    def recvline(self):
        return self.process.stdout.readline().decode('utf8')

    def recv_n(self, n):
        return self.process.stdout.read(n).decode('utf8')

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
        self.process.stdin.write(final_bytes)
        self.process.stdin.flush()

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


command = ['python', 'want_right.py']

pi = ProcessInteraction(command)
for i in range(2):
    content = pi.recvuntil_re(r'input (\d+): ')
    print(content[0])
    num = content[1].group(1)
    print(repr(num))
    pi.sendline(num)
content = pi.recvline()
print(content)
