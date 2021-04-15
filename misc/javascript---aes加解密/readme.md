使用javascript的crypto模块，AES加解密  
注意iv需要自己传递，这里拼在了密文前面  

```javascript
const { randomBytes, scryptSync, createCipheriv, createDecipheriv } = require('crypto');

const algorithm = 'aes-256-cbc';

function encrypt (text, password) {
    const iv = randomBytes(16);
    const secretKey = scryptSync(password, 'salt', 32);

    const cipher = createCipheriv(algorithm, secretKey, iv);
    const encrypted = Buffer.concat([cipher.update(text), cipher.final()]);

    return [iv.toString('hex'), encrypted.toString('hex')].join('');
};


function decrypt (hex_str, password) {
    const iv = Buffer.from(hex_str.substr(0, 32), 'hex');
    const encrypted = Buffer.from(hex_str.substr(32), 'hex');
    const secretKey = scryptSync(password, 'salt', 32);

    const decipher = createDecipheriv(algorithm, secretKey, iv);
    const decrpyted = Buffer.concat([decipher.update(encrypted), decipher.final()]);

    return decrpyted.toString();
};


const encrypted = encrypt('Hello World!', 'yesssss');
console.log(encrypted);

const decrpyted = decrypt(encrypted, 'yesssss');
console.log(decrpyted);
```

参考链接：  
https://nodejs.org/api/crypto.html  
https://attacomsian.com/blog/nodejs-encrypt-decrypt-data  
