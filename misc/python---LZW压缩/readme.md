# python---LZW压缩

其实不懂，暂时记一下代码  

```python
def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
            if dict_size == 65535:
                if w:
                    result.append(dictionary[w])
                w = ""
                dict_size = 256
                dictionary = {chr(i): i for i in range(dict_size)}

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from cStringIO import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    it = iter(compressed)
    for k in it:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
        if dict_size == 65535:
            dict_size = 256
            dictionary = {i: chr(i) for i in range(dict_size)}
            w = chr(next(it))
            result.write(w)

    return result.getvalue()


# How to use:
with open("./flag", 'r') as fp:
   data = fp.read()

compressed = compress(data)

import struct
with open("flag.enc", 'wb') as fp:
   for i in compressed:
       fp.write(struct.pack('H', i))

with open("flag.enc", 'r') as fp:
   comp = fp.read()

compressed = []
for i in range(len(comp)/2):
   d = comp[i*2:i*2+2]
   num = struct.unpack('H',d)[0]
   compressed.append(num)

decompressed = decompress(compressed)


with open("py.dec", 'w') as fp:
   fp.write(decompressed)
```


算法相关解释: https://segmentfault.com/a/1190000011425787  


2019/11/3  
