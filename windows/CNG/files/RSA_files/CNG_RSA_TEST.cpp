#include <Windows.h>
#include <stdio.h>
#include <bcrypt.h>
#pragma comment(lib, "Bcrypt.lib")

TCHAR szPubKeyFile[MAX_PATH] = L"public.key";  // 公钥路径
TCHAR szPriKeyFile[MAX_PATH] = L"private.key"; // 私钥路径，此文件会包含公钥
TCHAR rawFile[MAX_PATH] = L"raw.txt";          // 明文文件
TCHAR encryptedFile[MAX_PATH] = L"raw.enc";    // 加密后的文件
TCHAR decryptedFile[MAX_PATH] = L"raw.dec";    // 解密后的文件

int generateKeyFiles()
{
    BCRYPT_HANDLE m_hProv;
    BCRYPT_KEY_HANDLE m_hKey;
    BCryptOpenAlgorithmProvider(
        &m_hProv,
        BCRYPT_RSA_ALGORITHM,
        NULL,
        0);
    BCryptGenerateKeyPair(
        m_hProv,
        &m_hKey,
        2048,
        0);
    BCryptFinalizeKeyPair(
        m_hKey,
        0);
    // 导出公钥
    ULONG pubcbData;
    BCryptExportKey(
        m_hKey,
        NULL,
        BCRYPT_RSAPUBLIC_BLOB,
        NULL,
        0,
        &pubcbData,
        0);
    UCHAR pubpbBlob[4096];
    ULONG pubcbBlob;
    BCryptExportKey(
        m_hKey,
        NULL,
        BCRYPT_RSAPUBLIC_BLOB,
        pubpbBlob,
        pubcbBlob,
        &pubcbBlob,
        0);
    HANDLE pubhFile = CreateFile(
        szPubKeyFile,
        GENERIC_WRITE,
        FILE_SHARE_READ,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);
    WriteFile(
        pubhFile,
        pubpbBlob,
        pubcbBlob,
        &pubcbData,
        0);
    CloseHandle(pubhFile);
    // 导出私钥
    ULONG pricbData;
    BCryptExportKey(
        m_hKey,
        NULL,
        BCRYPT_RSAPRIVATE_BLOB,
        NULL,
        0,
        &pricbData,
        0);
    UCHAR pripbBlob[4096];
    ULONG pricbBlob;
    BCryptExportKey(
        m_hKey,
        NULL,
        BCRYPT_RSAPRIVATE_BLOB,
        pripbBlob,
        pricbBlob,
        &pricbBlob,
        0);
    HANDLE prihFile = CreateFile(
        szPriKeyFile,
        GENERIC_WRITE,
        FILE_SHARE_READ,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);
    WriteFile(
        prihFile,
        pripbBlob,
        pricbBlob,
        &pricbData,
        0);
    CloseHandle(prihFile);
    BCryptCloseAlgorithmProvider(m_hProv, 0);
    BCryptDestroyKey(m_hKey);
    printf("[+] key generated: %ls %ls.\n", szPubKeyFile, szPriKeyFile);
    return 0;
}

int writeRawFile()
{
    HANDLE hFile = CreateFile(
        rawFile,
        GENERIC_WRITE,
        FILE_SHARE_READ,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    char theContent[] = "Hello World!";
    DWORD dwBytesToWrite = strlen(theContent);
    DWORD dwBytesWritten = 0;
    WriteFile(
        hFile,
        theContent,
        dwBytesToWrite,
        &dwBytesWritten,
        NULL);

    CloseHandle(hFile);
    printf("[+] rawfile written: %ls.\n", rawFile);
    return 0;
}

int readPubEncData()
{
    BCRYPT_HANDLE m_hProv;
    BCRYPT_KEY_HANDLE m_hKey;
    BCryptOpenAlgorithmProvider(
        &m_hProv,
        BCRYPT_RSA_ALGORITHM,
        NULL,
        0);

    UCHAR abBlob[4096];
    ULONG cbBlob = 0;
    HANDLE hFile = CreateFile(
        szPubKeyFile,
        GENERIC_READ,
        FILE_SHARE_READ,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    ReadFile(
        hFile,
        abBlob,
        sizeof(abBlob),
        &cbBlob,
        0);

    BCryptImportKeyPair(
        m_hProv,
        NULL,
        BCRYPT_RSAPUBLIC_BLOB,
        &m_hKey,
        abBlob,
        cbBlob,
        0);
    CloseHandle(hFile);

    HANDLE rawhFile = CreateFile(
        rawFile,               // file to open
        GENERIC_READ,          // open for reading
        FILE_SHARE_READ,       // share for reading
        NULL,                  // default security
        OPEN_EXISTING,         // existing file only
        FILE_ATTRIBUTE_NORMAL, // normal file
        NULL);                 // no attr. template

    int theSize = GetFileSize(rawhFile, NULL);

    DWORD dwBytesRead = 0;
    UCHAR *rawBuffer = (UCHAR *)malloc((theSize + 1) * sizeof(UCHAR));
    ReadFile(rawhFile, rawBuffer, theSize, &dwBytesRead, NULL);
    rawBuffer[theSize] = 0;
    CloseHandle(rawhFile);

    ULONG cbEncryptedData;
    BCryptEncrypt(m_hKey,
                  rawBuffer,
                  theSize,
                  NULL,
                  NULL,
                  0,
                  NULL,
                  0,
                  &cbEncryptedData,
                  0);

    PUCHAR encryptedBuffer = (PUCHAR)HeapAlloc(GetProcessHeap(), 0, cbEncryptedData);
    memset(encryptedBuffer, 0, cbEncryptedData);
    ULONG pcbResult;
    BCryptEncrypt(
        m_hKey,
        rawBuffer,
        theSize,
        NULL,
        NULL,
        NULL,
        encryptedBuffer,
        cbEncryptedData,
        &pcbResult,
        BCRYPT_PAD_PKCS1);

    HANDLE enchFile = CreateFile(
        encryptedFile,
        GENERIC_WRITE,
        FILE_SHARE_READ,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    DWORD dwBytesWritten = 0;
    WriteFile(
        enchFile,
        encryptedBuffer,
        cbEncryptedData,
        &dwBytesWritten,
        NULL);

    CloseHandle(enchFile);

    free(rawBuffer);
    HeapFree(GetProcessHeap(), 0, encryptedBuffer);

    BCryptDestroyKey(m_hKey);
    BCryptCloseAlgorithmProvider(m_hProv, 0);
    printf("[+] file encrypted: %ls.\n", encryptedFile);
    return 0;
};

int readPriDecData()
{
    BCRYPT_HANDLE m_hProv;
    BCRYPT_KEY_HANDLE m_hKey;
    BCryptOpenAlgorithmProvider(
        &m_hProv,
        BCRYPT_RSA_ALGORITHM,
        NULL,
        0);

    UCHAR abBlob[4096];
    ULONG cbBlob = 0;
    HANDLE hFile = CreateFile(
        szPriKeyFile,
        GENERIC_READ,
        FILE_SHARE_READ,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    ReadFile(
        hFile,
        abBlob,
        sizeof(abBlob),
        &cbBlob,
        0);

    BCryptImportKeyPair(
        m_hProv,
        NULL,
        BCRYPT_RSAPRIVATE_BLOB,
        &m_hKey,
        abBlob,
        cbBlob,
        0);
    CloseHandle(hFile);

    HANDLE enchFile = CreateFile(
        encryptedFile,         // file to open
        GENERIC_READ,          // open for reading
        FILE_SHARE_READ,       // share for reading
        NULL,                  // default security
        OPEN_EXISTING,         // existing file only
        FILE_ATTRIBUTE_NORMAL, // normal file
        NULL);                 // no attr. template

    int theSize = GetFileSize(enchFile, NULL);

    DWORD dwBytesRead = 0;
    UCHAR decBuffer[0x200];
    ReadFile(enchFile, decBuffer, theSize, &dwBytesRead, NULL);
    decBuffer[theSize] = 0;
    CloseHandle(enchFile);

    ULONG cbDecryptedData;
    UCHAR decryptedData[0x20];
    BCryptDecrypt(
        m_hKey,
        decBuffer,
        theSize,
        NULL,
        NULL,
        0,
        decryptedData,
        cbDecryptedData,
        &cbDecryptedData,
        BCRYPT_PAD_PKCS1);

    HANDLE dechFile = CreateFile(
        decryptedFile,
        GENERIC_WRITE,
        FILE_SHARE_READ,
        NULL,
        CREATE_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    DWORD dwBytesWritten = 0;
    WriteFile(
        dechFile,
        decryptedData,
        cbDecryptedData,
        &dwBytesWritten,
        NULL);

    CloseHandle(dechFile);

    BCryptDestroyKey(m_hKey);
    BCryptCloseAlgorithmProvider(m_hProv, 0);
    printf("[+] file decrypted: %ls.\n", decryptedFile);
    return 0;
};

int main()
{
    // 1. 生成密钥对，写入文件
    generateKeyFiles();
    // 2. 写raw.txt
    writeRawFile();
    // 3. 读公钥，加密数据
    readPubEncData();
    // 4. 读私钥，解密数据
    readPriDecData();

    return 0;
}