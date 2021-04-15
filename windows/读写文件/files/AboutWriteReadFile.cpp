#include <Windows.h>
#include <stdio.h>


int ReadTheFile(LPCWSTR filePath)
{
    HANDLE hFile;

    hFile = CreateFile(
        filePath,               // file to open
        GENERIC_READ,          // open for reading
        FILE_SHARE_READ,       // share for reading
        NULL,                  // default security
        OPEN_EXISTING,         // existing file only
        FILE_ATTRIBUTE_NORMAL, // normal file
        NULL);                 // no attr. template

    if (hFile == INVALID_HANDLE_VALUE) {
        wprintf(L"[!] error to open the file %s: GetLastError=%08x\n", filePath, GetLastError());
        return 1;
    }

    int theSize = GetFileSize(hFile, NULL);

    DWORD dwBytesRead = 0;
    char* theBuffer = (char*)malloc((theSize+1) * sizeof(char));

    if (FALSE == ReadFile(hFile, theBuffer, theSize, &dwBytesRead, NULL)) {
        printf("[!] error to read the file: GetLastError=%08x\n", GetLastError());
        CloseHandle(hFile);
        return 1;
    }
   
    theBuffer[theSize] = 0;

    printf("[*] read: '%s' from ", theBuffer);
    wprintf(L"%s.\n", filePath);

    CloseHandle(hFile);
    free(theBuffer);

    return 0;
}


int WriteTheFile(LPCWSTR filePath)
{
    HANDLE hFile;

    hFile = CreateFile(
        filePath,               // file to open
        GENERIC_WRITE,          // open for writing
        FILE_SHARE_READ,       // share for reading
        NULL,                  // default security
        CREATE_ALWAYS,         // always create file
        FILE_ATTRIBUTE_NORMAL, // normal file
        NULL);                 // no attr. template

    if (hFile == INVALID_HANDLE_VALUE) {
        wprintf(L"[!] error to open the file %s: GetLastError=%08x\n", filePath, GetLastError());
        return 1;
    }

    char theContent[] = "Hello World!";
    DWORD dwBytesToWrite = strlen(theContent);
    DWORD dwBytesWritten = 0;
    BOOL bErrorFlag = WriteFile(
        hFile,           // open file handle
        theContent,      // start of data to write
        dwBytesToWrite,  // number of bytes to write
        &dwBytesWritten, // number of bytes that were written
        NULL);            // no overlapped structure

    if (bErrorFlag == FALSE)
    {
        wprintf(L"[!] error to write the file : %s GetLastError=%08x\n", filePath, GetLastError());
    }
    else {
        if (dwBytesWritten != dwBytesToWrite)
        {
            printf("[!] error: dwBytesWritten != dwBytesToWrite\n");
        }
        else
        {
            printf("[*] wrote '%s' to ", theContent);
            wprintf(L"%s.\n", filePath);
        }
    }

    CloseHandle(hFile);

    return 0;
}


int main()
{
    LPCWSTR filePath = L"good.txt";
    WriteTheFile(filePath);
    ReadTheFile(filePath);

    return 0;
}
