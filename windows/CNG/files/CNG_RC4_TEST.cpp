// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (C) Microsoft. All rights reserved.
/*++

Abstract:
	Sample program for RC4 encryption using CNG

--*/

#include <windows.h>
#include <stdio.h>
#include <bcrypt.h>
#pragma comment(lib, "Bcrypt.lib")

#define NT_SUCCESS(Status)          (((NTSTATUS)(Status)) >= 0)

#define STATUS_UNSUCCESSFUL         ((NTSTATUS)0xC0000001L)


const BYTE rgbPlaintext[] =
{
	0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
	0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F
};

static const BYTE rgbRC4Key[] =
{
	0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
	0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F
};

void PrintBytes(
	IN const BYTE* pbPrintData,
	IN DWORD    cbDataLen)
{
	DWORD dwCount = 0;

	for (dwCount = 0; dwCount < cbDataLen; dwCount++)
	{
		printf("0x%02x, ", pbPrintData[dwCount]);

		if (0 == (dwCount + 1) % 10) putchar('\n');
	}

}

void __cdecl wmain(
	int                      argc,
	__in_ecount(argc) LPWSTR* wargv)
{

	BCRYPT_ALG_HANDLE       hRC4Alg = NULL;
	BCRYPT_KEY_HANDLE       hKey = NULL;
	NTSTATUS                status = STATUS_UNSUCCESSFUL;
	DWORD                   cbCipherText = 0,
							cbPlainText = 0,
							cbData = 0,
							cbKeyObject = 0,
							cbBlockLen = 0,
							cbBlob = 0;
	PBYTE                   pbCipherText = NULL,
							pbPlainText = NULL,
							pbKeyObject = NULL,
							pbBlob = NULL;

	UNREFERENCED_PARAMETER(argc);
	UNREFERENCED_PARAMETER(wargv);


	printf("\nrgbPlaintext:\n");
	PrintBytes(rgbPlaintext, sizeof(rgbPlaintext));
	printf("\nrgbRC4Key:\n");
	PrintBytes(rgbRC4Key, sizeof(rgbRC4Key));
	printf("\n\n");


	// Open an algorithm handle.
	if (!NT_SUCCESS(status = BCryptOpenAlgorithmProvider(
		&hRC4Alg,
		BCRYPT_RC4_ALGORITHM,
		NULL,
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptOpenAlgorithmProvider\n", status);
		goto Cleanup;
	}

	// Calculate the size of the buffer to hold the KeyObject.
	if (!NT_SUCCESS(status = BCryptGetProperty(
		hRC4Alg,
		BCRYPT_OBJECT_LENGTH,
		(PBYTE)&cbKeyObject,
		sizeof(DWORD),
		&cbData,
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptGetProperty\n", status);
		goto Cleanup;
	}

	// Allocate the key object on the heap.
	pbKeyObject = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbKeyObject);
	if (NULL == pbKeyObject)
	{
		wprintf(L"**** memory allocation failed\n");
		goto Cleanup;
	}


	// Generate the key from supplied input key bytes.
	if (!NT_SUCCESS(status = BCryptGenerateSymmetricKey(
		hRC4Alg,
		&hKey,
		pbKeyObject,
		cbKeyObject,
		(PBYTE)rgbRC4Key,
		sizeof(rgbRC4Key),
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptGenerateSymmetricKey\n", status);
		goto Cleanup;
	}


	// Save another copy of the key for later.
	if (!NT_SUCCESS(status = BCryptExportKey(
		hKey,
		NULL,
		BCRYPT_OPAQUE_KEY_BLOB,
		NULL,
		0,
		&cbBlob,
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptExportKey\n", status);
		goto Cleanup;
	}


	// Allocate the buffer to hold the BLOB.
	pbBlob = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbBlob);
	if (NULL == pbBlob)
	{
		wprintf(L"**** memory allocation failed\n");
		goto Cleanup;
	}

	if (!NT_SUCCESS(status = BCryptExportKey(
		hKey,
		NULL,
		BCRYPT_OPAQUE_KEY_BLOB,
		pbBlob,
		cbBlob,
		&cbBlob,
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptExportKey\n", status);
		goto Cleanup;
	}

	cbPlainText = sizeof(rgbPlaintext);
	pbPlainText = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPlainText);
	if (NULL == pbPlainText)
	{
		wprintf(L"**** memory allocation failed\n");
		goto Cleanup;
	}

	memcpy(pbPlainText, rgbPlaintext, sizeof(rgbPlaintext));

	//
	// Get the output buffer size.
	//
	if (!NT_SUCCESS(status = BCryptEncrypt(
		hKey,
		pbPlainText,
		cbPlainText,
		NULL,
		NULL,
		NULL,
		NULL,
		0,
		&cbCipherText,
		NULL)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptEncrypt\n", status);
		goto Cleanup;
	}

	pbCipherText = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbCipherText);
	if (NULL == pbCipherText)
	{
		wprintf(L"**** memory allocation failed\n");
		goto Cleanup;
	}

	// Use the key to encrypt the plaintext buffer.
	// For block sized messages, block padding will add an extra block.
	if (!NT_SUCCESS(status = BCryptEncrypt(
		hKey,
		pbPlainText,
		cbPlainText,
		NULL,
		NULL,
		NULL,
		pbCipherText,
		cbCipherText,
		&cbData,
		NULL)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptEncrypt\n", status);
		goto Cleanup;
	}


	printf("\npbCipherText:\n");
	PrintBytes(pbCipherText, cbCipherText);
	printf("\n\n");


	// Destroy the key and reimport from saved BLOB.
	if (!NT_SUCCESS(status = BCryptDestroyKey(hKey)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptDestroyKey\n", status);
		goto Cleanup;
	}
	hKey = 0;

	if (pbPlainText)
	{
		HeapFree(GetProcessHeap(), 0, pbPlainText);
	}

	pbPlainText = NULL;

	// We can reuse the key object.
	memset(pbKeyObject, 0, cbKeyObject);


	if (!NT_SUCCESS(status = BCryptImportKey(
		hRC4Alg,
		NULL,
		BCRYPT_OPAQUE_KEY_BLOB,
		&hKey,
		pbKeyObject,
		cbKeyObject,
		pbBlob,
		cbBlob,
		0)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptGenerateSymmetricKey\n", status);
		goto Cleanup;
	}


	//
	// Get the output buffer size.
	//
	if (!NT_SUCCESS(status = BCryptDecrypt(
		hKey,
		pbCipherText,
		cbCipherText,
		NULL,
		NULL,
		NULL,
		NULL,
		0,
		&cbPlainText,
		NULL)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptDecrypt\n", status);
		goto Cleanup;
	}

	pbPlainText = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPlainText);
	if (NULL == pbPlainText)
	{
		wprintf(L"**** memory allocation failed\n");
		goto Cleanup;
	}

	if (!NT_SUCCESS(status = BCryptDecrypt(
		hKey,
		pbCipherText,
		cbCipherText,
		NULL,
		NULL,
		NULL,
		pbPlainText,
		cbPlainText,
		&cbPlainText,
		NULL)))
	{
		wprintf(L"**** Error 0x%x returned by BCryptDecrypt\n", status);
		goto Cleanup;
	}


	printf("\ndecrypted pbPlainText:\n");
	PrintBytes(pbPlainText, cbPlainText);
	printf("\n\n");


	if (0 != memcmp(pbPlainText, (PBYTE)rgbPlaintext, sizeof(rgbPlaintext)))
	{
		wprintf(L"Expected decrypted text comparison failed.\n");
		goto Cleanup;
	}

	wprintf(L"Success!\n");


Cleanup:

	if (hRC4Alg)
	{
		BCryptCloseAlgorithmProvider(hRC4Alg, 0);
	}

	if (hKey)
	{
		BCryptDestroyKey(hKey);
	}

	if (pbCipherText)
	{
		HeapFree(GetProcessHeap(), 0, pbCipherText);
	}

	if (pbPlainText)
	{
		HeapFree(GetProcessHeap(), 0, pbPlainText);
	}

	if (pbKeyObject)
	{
		HeapFree(GetProcessHeap(), 0, pbKeyObject);
	}

}