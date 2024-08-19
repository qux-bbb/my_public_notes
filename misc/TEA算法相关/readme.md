# TEA算法相关

## TEA
TEA, Tiny Encryption Algorithm, 微型加密算法  
```c
#include <stdint.h>

void encrypt (uint32_t v[2], const uint32_t k[4]) {
    uint32_t v0=v[0], v1=v[1], sum=0, i;           /* set up */
    uint32_t delta=0x9E3779B9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i<32; i++) {                         /* basic cycle start */
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

void decrypt (uint32_t v[2], const uint32_t k[4]) {
    uint32_t v0=v[0], v1=v[1], sum=0xC6EF3720, i;  /* set up; sum is (delta << 5) & 0xFFFFFFFF */
    uint32_t delta=0x9E3779B9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i<32; i++) {                         /* basic cycle start */
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}
```

## XTEA
XTEA, eXtended TEA, 扩展的TEA算法, 使用更复杂的key处理，移位、异或、相加的重新排布  
```c
#include <stdint.h>

/* take 64 bits of data in v[0] and v[1] and 128 bits of key[0] - key[3] */

void encipher(unsigned int num_rounds, uint32_t v[2], uint32_t const key[4]) {
    unsigned int i;
    uint32_t v0=v[0], v1=v[1], sum=0, delta=0x9E3779B9;
    for (i=0; i < num_rounds; i++) {
        v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
        sum += delta;
        v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
    }
    v[0]=v0; v[1]=v1;
}

void decipher(unsigned int num_rounds, uint32_t v[2], uint32_t const key[4]) {
    unsigned int i;
    uint32_t v0=v[0], v1=v[1], delta=0x9E3779B9, sum=delta*num_rounds;
    for (i=0; i < num_rounds; i++) {
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
        sum -= delta;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
    }
    v[0]=v0; v[1]=v1;
}
```

## XXTEA
XXTEA, Corrected Block TEA  
```c
#include <stdio.h>  
#include <stdlib.h>  
#include <stdint.h>  
#include <string.h>  

#define DELTA 0x9e3779b9
#define MX (((z>>5^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))

void btea(uint32_t* v, int n, uint32_t const key[4]) {
    uint32_t y, z, sum;
    unsigned p, rounds, e;
    if (n > 1) {          /* Coding Part */
        rounds = 6 + 52 / n;
        sum = 0;
        z = v[n - 1];
        do {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p = 0; p < n - 1; p++) {
                y = v[p + 1];
                z = v[p] += MX;
            }
            y = v[0];
            z = v[n - 1] += MX;
        } while (--rounds);
    }
    else if (n < -1) {  /* Decoding Part */
        n = -n;
        rounds = 6 + 52 / n;
        sum = rounds * DELTA;
        y = v[0];
        do {
            e = (sum >> 2) & 3;
            for (p = n - 1; p > 0; p--) {
                z = v[p - 1];
                y = v[p] -= MX;
            }
            z = v[n - 1];
            y = v[0] -= MX;
            sum -= DELTA;
        } while (--rounds);
    }
}

int main() {
    char text[] = "Improve the world!";
    char key[] = "Just do it.";

    // 1. 新分配空间，用空字节填充text至4的倍数，最后使用4字节保存明文长度
    int text_len = strlen(text);
    int text_size = (text_len + 3) / 4 * 4 + 4;
    char* padded_text = (char*)malloc(text_size);
    memset(padded_text, 0, text_size);
    memcpy(padded_text, text, text_len);
    *(uint32_t*)(padded_text + text_size - 4) = text_len;

    // 2. 新分配空间，用空字节填充key为16个字节
    int key_len = strlen(key);
    //int key_size = (key_len + 3) / 4 * 4;
    int key_size = 16;
    char* padded_key = (char*)malloc(key_size);
    memset(padded_key, 0, key_size);
    memcpy(padded_key, key, key_len);

    // 3. 加密，输出加密后的内容
    uint32_t* text_uint32 = (uint32_t*)padded_text;
    uint32_t* key_uint32 = (uint32_t*)padded_key;
    btea(text_uint32, text_size / 4, key_uint32);
    printf("encrypted:\n");
    for (int i = 0; i < text_size / 4; i++) {
        printf("0x%08x,", text_uint32[i]);
    }
    printf("\n");
    for (int i = 0; i < text_size / 4; i++) {
        unsigned char bytes[4];
        memcpy(bytes, &text_uint32[i], 4); // 将uint32_t值复制到字节数组中
        for (int j = 0; j < 4; j++) {
            printf("%02x", bytes[j]);
            if (j < 3) {
                printf(" "); // 在字节之间添加空格，除了最后一个字节
            }
        }
        if (i < text_size - 1) {
            printf(" "); // 在每个uint32_t之间添加空格，除了最后一个
        }
    }
    printf("\n");

    // 4. 解密，输出解密后的内容
    btea(text_uint32, -text_size / 4, key_uint32);
    int original_len = *(uint32_t*)(text_uint32 + text_size / 4 - 1);
    printf("decrypted:\n%.*s\n", original_len, text_uint32);

    free(padded_text);
    free(padded_key);

    return 0;
}
/*
encrypted:
0x90f08367,0x9c5c4986,0x8f86feb4,0x2b85edd6,0x67b79425,0xdaf04cd4,
67 83 f0 90 86 49 5c 9c b4 fe 86 8f d6 ed 85 2b 25 94 b7 67 d4 4c f0 da
decrypted:
Improve the world!
*/
```

## 其它
很容易根据常数 0x9E3779B9 判断加密算法是否和TEA相关，所以有时会换成 -0x61C88647 的形式。  


## 原链接
1. https://en.wikipedia.org/wiki/Tiny_Encryption_Algorithm
2. https://en.wikipedia.org/wiki/XTEA
3. https://en.wikipedia.org/wiki/XXTEA


---
2021/11/16  
