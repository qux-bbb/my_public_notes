python计算crc32，python2和python3均可  

```python
import binascii

a = b'hello'
b = '{:0>8x}'.format(binascii.crc32(a))
```