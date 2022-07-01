# c---rc4

RC4, Rivest Cipher 4, Ronald Rivest 开发的对称加密算法。  
该算法为流加密算法，密钥长度可变，密钥生成的序列和明文异或即得到密文，加解密完全相同。  

```cpp
//程序开始
#include<stdio.h>
#include<string.h>

/*初始化函数*/
void rc4_init(unsigned char* s, unsigned char* key, unsigned long Len)
{
	int i = 0, j = 0;
	unsigned char tmp = 0;
	for (i = 0; i < 256; i++)
	{
		s[i] = i;
	}
	for (i = 0; i < 256; i++)
	{
		j = (j + s[i] + key[i % Len]) % 256;
		tmp = s[i];
		s[i] = s[j];  //交换s[i]和s[j]
		s[j] = tmp;
	}
}

/*加解密*/
void rc4_crypt(unsigned char* s, unsigned char* Data, unsigned long Len)
{
	int x = 0, y = 0, k = 0;
	unsigned long i = 0;
	unsigned char tmp;
	for (i = 0; i < Len; i++)
	{
		x = (x + 1) % 256;
		y = (y + s[x]) % 256;
		tmp = s[x];
		s[x] = s[y];  //交换s[x]和s[y]
		s[y] = tmp;
		k = (s[x] + s[y]) % 256;
		Data[i] ^= s[k];
	}
}

int main()
{
	unsigned char s[256] = { 0 }, s2[256] = { 0 };  //S-box
	char key[256] = { "justfortest" };
	char pData[512] = "这是一个用来加密的数据Data";
	unsigned long len = strlen(pData);
	int i;

	printf("pData=\"%s\"\n", pData);
	printf("key=\"%s\",length=%d\n\n", key, strlen(key));
	rc4_init(s, (unsigned char*)key, strlen(key));  //已经完成了初始化
	printf("完成对S[i]的初始化，如下：\n");
	for (i = 0; i < 256; i++)
	{
		printf("%02X", s[i]);
		if (i && (i + 1) % 16 == 0)putchar('\n');
	}
	printf("\n\n");
	for (i = 0; i < 256; i++)  //用s2[i]暂时保留经过初始化的s[i]，解密的时候再用
	{
		s2[i] = s[i];
	}

	printf("已经初始化，现在加密:\n");
	rc4_crypt(s, (unsigned char*)pData, len);  //加密
	printf("pData=\"%s\"\n\n", pData);

	printf("已经加密，现在解密:\n");
	//rc4_init(s,(unsignedchar*)key,strlen(key));  //初始化密钥
	rc4_crypt(s2, (unsigned char*)pData, len);  //解密
	printf("pData=\"%s\"\n\n", pData);

	return 0;
}

//程序完
```


原链接: https://baike.baidu.com/item/RC4/3454548  


2022/1/23  
