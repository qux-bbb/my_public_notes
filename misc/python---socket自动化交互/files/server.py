# coding:utf8
# python3

import random
import socket

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9999

# 绑定端口号
serversocket.bind(('', port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    try:
        print('等待连接...')
        # 建立客户端连接
        clientsocket, addr = serversocket.accept()
        print("连接地址: ", addr)

        first_num = str(random.randint(0, 10))
        second_num = str(random.randint(0, 10))

        clientsocket.send('input {}: '.format(first_num).encode('utf8'))
        first_input = clientsocket.recv(10).decode('utf8').strip()
        clientsocket.send('input {}: '.format(second_num).encode('utf8'))
        second_input = clientsocket.recv(10).decode('utf8').strip()

        print(first_input)
        print(second_input)

        if first_num == first_input and second_num == second_input:
            clientsocket.send('Right!\n'.encode('utf8'))
        else:
            clientsocket.send('Wrong!\n'.encode('utf8'))
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
    except KeyboardInterrupt as identifier:
        print('程序被手动停止')
        break

serversocket.close()
