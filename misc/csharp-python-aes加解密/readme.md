# csharp-python-aes加解密

C#的aes加解密，用python再做一遍  

```csharp
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace CSharpCmdHello1
{
    class Program
    {
        static void Main(string[] args)
        {
            string message = "hello world";
            string password = "secret";
            string salt = "just a salt";

            string cipherText = AesEncrypt(password, salt, message);
            Console.WriteLine(cipherText);

            string plainText = AesDecrypt(password, salt, cipherText);
            Console.WriteLine(plainText);
            Console.ReadKey();
            /*
            sQFW2pV+B7T6t0h4xu8Smw==
            hello world
            */
        }

        static string AesEncrypt(string password, string salt, string message)
        {
            byte[] saltBytes = Encoding.Default.GetBytes(salt);
            byte[] messageBytes = Encoding.Default.GetBytes(message);

            Aes aes = Aes.Create();
            Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(password, saltBytes);
            aes.Key = rfc2898DeriveBytes.GetBytes(32);
            aes.IV = rfc2898DeriveBytes.GetBytes(16);
            MemoryStream memoryStream = new MemoryStream();
            CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateEncryptor(), CryptoStreamMode.Write);
            cryptoStream.Write(messageBytes, 0, messageBytes.Length);
            cryptoStream.Close();
            string cipherText = Convert.ToBase64String(memoryStream.ToArray());
            memoryStream.Close();
            aes.Dispose();

            return cipherText;
        }

        static string AesDecrypt(string password, string salt, string cipherText)
        {
            byte[] saltBytes = Encoding.Default.GetBytes(salt);
            byte[] cipherBytes = Convert.FromBase64String(cipherText);
            Aes aes = Aes.Create();
            Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(password, saltBytes);
            aes.Key = rfc2898DeriveBytes.GetBytes(32);
            aes.IV = rfc2898DeriveBytes.GetBytes(16);
            MemoryStream memoryStream = new MemoryStream();
            CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateDecryptor(), CryptoStreamMode.Write);
            cryptoStream.Write(cipherBytes, 0, cipherBytes.Length);
            cryptoStream.Close();
            string plainText = Encoding.Default.GetString(memoryStream.ToArray());
            memoryStream.Close();
            aes.Dispose();
            return plainText;
        }
    }
}
```

```python
# coding:utf8
# python3

import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(password, salt, message):
    message = pad(message, 16)
    key_iv = PBKDF2(password, salt, dkLen=48)
    key = key_iv[:32]  # 前32位
    iv = key_iv[32:]  # 后16位
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(message)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

def aes_decrypt(password, salt, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    key_iv = PBKDF2(password, salt, dkLen=48)
    key = key_iv[:32]  # 前32位
    iv = key_iv[32:]  # 后16位
    obj = AES.new(key, AES.MODE_CBC, iv)
    plaintext = obj.decrypt(ciphertext)
    plaintext = unpad(plaintext, 16)
    return plaintext


def main():
    message = b'hello world'
    password = 'secret'
    salt = b'just a salt'

    ciphertext = aes_encrypt(password, salt, message)
    print(ciphertext)

    plaintext = aes_decrypt(password, salt, ciphertext)
    print(plaintext)


if __name__ == '__main__':
    main()

# b'sQFW2pV+B7T6t0h4xu8Smw=='
# b'hello world'
```


---
2021/12/9  
