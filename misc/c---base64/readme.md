# c---base64

用c写一下base64  

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char baseArr[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

char FindIndex(char theChar)
{
	for (int i = 0; i < 65; i++)
	{
		if (baseArr[i] == theChar)
			return i;
	}

	return 64;
}

void Base64Encode(char* data, char* encodedData, long dataLen, long encodedDataLen)
{
	long j = 0;
	for (long i = 0; i < dataLen; i += 3)
	{
		// restDataLen should >= 1
		long restDataLen = dataLen - i;

		encodedData[j++] = baseArr[data[i] >> 2];
		if (restDataLen == 1)
		{
			encodedData[j++] = baseArr[(data[i] & 0b11) << 4];
			encodedData[j++] = baseArr[64];
			encodedData[j++] = baseArr[64];
		}
		else
		{
			encodedData[j++] = baseArr[((data[i] & 0b11) << 4) | (data[i + 1] >> 4)];
			if (restDataLen == 2)
			{
				encodedData[j++] = baseArr[(data[i + 1] & 0b1111) << 2];
				encodedData[j++] = baseArr[64];
			}
			else  // when restDataLen >= 3
			{
				encodedData[j++] = baseArr[((data[i + 1] & 0b1111) << 2) | (data[i + 2] >> 6)];
				encodedData[j++] = baseArr[data[i + 2] & 0b111111];
			}
		}
	}

	return;
}

void Base64Decode(char* decodedData, char* encodedData, long decodedDataLen, long encodedDataLen)
{
	int j = 0;
	for (int i = 0; i < encodedDataLen; i+=4)
	{
		char n1 = FindIndex(encodedData[i]);
		char n2 = FindIndex(encodedData[i+1]);
		
		decodedData[j++] = (n1 << 2) | (n2 >> 4);
		if (encodedData[i + 2] != baseArr[64])
		{
			char n3 = FindIndex(encodedData[i + 2]);
			decodedData[j++] = (n2 << 4) | (n3 >> 2);
			if (encodedData[i+3] != baseArr[64])
			{
				char n4 = FindIndex(encodedData[i + 3]);
				decodedData[j++] = (n3 << 6) | n4;
			}
		}
	}

	return;
}


int main()
{
	char theData[] = "Hello, World!";
	printf("theData: %s\n", theData);

	long dataLen = strlen(theData);
	long encodedDataLen = (dataLen + 2) / 3 * 4;
	char* encodedData = (char*)malloc((encodedDataLen + 1) * sizeof(char));
	memset(encodedData, 0, (encodedDataLen + 1) * sizeof(char));
	Base64Encode((char *)theData, encodedData, dataLen, encodedDataLen);
	printf("encodedData: %s\n", encodedData);

	if (encodedDataLen % 4 != 0)
	{
		printf("encodedDataLen %% 4 != 0\n");
		return 0;
	}
	long decodedDataLen = encodedDataLen / 4 * 3;
	char* decodedData = (char*)malloc((decodedDataLen + 1) * sizeof(char));
	memset(decodedData, 0, (decodedDataLen + 1) * sizeof(char));
	Base64Decode(decodedData, encodedData, decodedDataLen, encodedDataLen);
	printf("decodedData: %s\n", decodedData);

	free(encodedData);
	free(decodedData);

	return 0;
}
```


2021/11/16  
