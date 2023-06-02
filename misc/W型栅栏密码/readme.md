# W型栅栏密码

```python

# coding:utf8

'''
helloworldgoodmorningxxxx 5
h       l       r       x
 e     r d     o n     x
  l   o   g   m   i   x
   l w     o d     n x
    o       o       g
hlrnerdonilogmiqlwodnxoog

7
5 1
3 3
1 5
7


helloworldgoodmorningxxxx 4
h     o     o     i     x
 e   w r   o d   n n   x
  l o   l g   m r   g x
   l     d     o     x
hooixewrodnnxlolgmrgxldox

5
3 1
1 3
5
'''

def enc(plain, num):
    matrix = [([0] * len(plain)) for i in range(num)]

    # 获取i的取值序列
    i_s = []
    for a in range(num):
        i_s.append(a)
    for a in range(num - 2, 0, -1):
        i_s.append(a)
    i_s_len = len(i_s)

    # 按规则写入
    i = 0
    for c in plain:
        matrix[i_s[i % i_s_len]][i] = c
        i += 1

    # 排除空值，从头到尾取出
    encrypted = ''
    for i in range(num):
        for j in range(len(plain)):
            if matrix[i][j]:
                encrypted += matrix[i][j]

    # 临时输出
    for i in range(num):
        for j in range(len(plain)):
            print matrix[i][j], ' ',
        print
    
    return encrypted


def dec(encrypted, num):
    matrix = [([0] * len(encrypted)) for i in range(num)]
    cur = 0
    for i in range(num):  # 按行来填
        # 生成每行空格个数的取值序列
        if i == 0:  # 第1行和最后一行，只需要一个取值就好了
            pair = [(num-(i+1))*2-1]
        elif i == num-1:
            pair = [i*2-1]
        else:
            pair = [(num-(i+1))*2-1, i*2-1]
        
        # 按规则填入
        pair_i = 0
        j = i
        while True:
            if cur < len(encrypted):
                matrix[i][j] = encrypted[cur]
            cur += 1
            j += pair[pair_i % len(pair)]+1  # 这里要加1，直接加间隔是不够的
            pair_i += 1
            if j >= len(encrypted):
                break

    # 临时输出
    for i in range(num):
        for j in range(len(encrypted)):
            print matrix[i][j], ' ',
        print

    # 获取i的取值序列
    i_s = []
    for a in range(num):
        i_s.append(a)
    for a in range(num - 2, 0, -1):
        i_s.append(a)
    i_s_len = len(i_s)
    # 按规则取出
    decrypted = ''
    for j in range(len(encrypted)):
        decrypted += matrix[i_s[j % i_s_len]][j]
    return decrypted


encrypted = enc('helloworldgoodmorningxxxx', 11)
print encrypted
decrypted = dec(encrypted, 11)
print decrypted

encrypted = 'ccehgyaefnpeoobe{lcirg}epriec_ora_g'
num = 5
print dec(encrypted, num)

'''
hooixewrodnnxlolgmrgxldox
helloworldgoodmorningxxxx
cyberpeace{railfence_cipher_gogogo}
'''

```


2019/9/4  
