# python2---哈希验证功能防爆破

摘自D3CTF  

```python
class signandverify(SocketServer.StreamRequestHandler):
    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
        digest = hashlib.sha256(proof.encode('utf-8')).hexdigest()
        self.request.sendall("sha256(XXXX+%s) == %s\n" % (proof[4:],digest))
        self.request.sendall('Give me XXXX:')
        x = self.rfile.readline().strip()
        if len(x) != 4 or hashlib.sha256((x+proof[4:])).hexdigest() != digest: 
            return False
        return True
```

2019/11/24  
