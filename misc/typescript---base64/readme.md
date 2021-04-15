这里有简单标准的方法  
```typescript
encoded = Buffer.from('hello').toString('base64')
decoded = Buffer.from(encoded, 'base64').toString()
console.log(encoded)
console.log(decoded)


encoded = Buffer.from('你好').toString('base64')
decoded = Buffer.from(encoded, 'base64').toString()
console.log(encoded)
console.log(decoded)
```


这是自己写的，汉字会出错，所以不要用，不过可以理解一下base64的原理  
```typescript
const baseDict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';

function base64encode(theString:string) {
    let encodedString = '';
    for (let i = 0; i < theString.length; i+=3) {
        if (theString.length-i >= 3) {
            // 剩余字符数>=3，正常操作
            const n1 = theString.charCodeAt(i);
            const n2 = theString.charCodeAt(i+1);
            const n3 = theString.charCodeAt(i+2);
            encodedString += baseDict[n1 >> 2];
            encodedString += baseDict[((n1 & 0b11) << 4) | (n2 >> 4)];
            encodedString += baseDict[((n2 & 0b1111) << 2) | (n3 >> 6)];
            encodedString += baseDict[n3 & 0b111111];
        } else if (theString.length-i == 2) {
            // 仅剩2个字符
            const n1 = theString.charCodeAt(i);
            const n2 = theString.charCodeAt(i+1);
            encodedString += baseDict[n1 >> 2];
            encodedString += baseDict[((n1 & 0b11) << 4) | (n2 >> 4)];
            encodedString += baseDict[(n2 & 0b1111) << 2];
            encodedString += baseDict[64];
        } else {
            // 仅剩1个字符
            const n1 = theString.charCodeAt(i);
            encodedString += baseDict[n1 >> 2];
            encodedString += baseDict[(n1 & 0b11) << 4];
            encodedString += baseDict[64];
            encodedString += baseDict[64];
        }
    }
    return encodedString;
}

function base64decode(theString:string) {
    let decodedString = '';
    for (let i = 0; i < theString.length; i+=4) {
        const n1 = baseDict.indexOf(theString[i]);
        const n2 = baseDict.indexOf(theString[i+1]);
        const n3 = baseDict.indexOf(theString[i+2]);
        const n4 = baseDict.indexOf(theString[i+3]);

        decodedString += String.fromCharCode((n1 << 2) | (n2 >> 4));
        if (n3 !== 64) {
            decodedString += String.fromCharCode(((n2 & 0b1111) << 4) | (n3 >> 2));
            if (n4 != 64) {
                decodedString += String.fromCharCode(((n3 & 0b11) << 6) | n4);
            }
        }
    }
    return decodedString;
}

let a = base64encode('hello');
console.log(a);
let b = base64decode(a);
console.log(b);
```
