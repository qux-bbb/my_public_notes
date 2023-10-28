# python3

import idaapi

def add_bulk_decompiler_comments(addr_comment_dict):
    print("开始批量添加反编译注释...")
    
    success_count = 0
    failure_count = 0

    for ea, comment in addr_comment_dict.items():
        cfunc = idaapi.decompile(ea)
        if not cfunc:
            print("失败：无法反编译函数位于 0x{:X} 的地址".format(ea))
            failure_count += 1
            continue

        tl = idaapi.treeloc_t()  # 创建一个 treeloc_t 对象，以指定注释的位置和类型
        tl.ea = ea
        tl.itp = idaapi.ITP_SEMI  # 普通注释

        try:
            cfunc.set_user_cmt(tl, comment)
            cfunc.save_user_cmts()
            print("成功：在 0x{:X} 添加注释 '{}'".format(ea, comment))
            success_count += 1
        except Exception as e:
            print("失败：无法在 0x{:X} 添加注释。错误：{}".format(ea, str(e)))
            failure_count += 1

    print("批量添加完成。成功：{}，失败：{}".format(success_count, failure_count))


# 使用示例
addr_comment_dict = {
    0x309A57F: "kernel32.dll.LoadLibraryA",
    0x309A5E6: "kernel32.dll.GetProcAddress",
    0x309F5CB: "kernel32.dll.GetProcessHeap",
    0x3092138: "ws2_32.dll.WSAStartup",
    0x3096668: "ntdll.dll.RtlAllocateHeap",
    0x3098862: "wininet.dll.InternetSetOptionA",
    0x309129B: "shell32.dll.SHGetFolderPathW",
    0x30912C7: "kernel32.dll.GetModuleFileNameW",
    0x309B8E1: "advapi32.dll.OpenProcessToken",
    0x3097A6A: "advapi32.dll.GetTokenInformation",
    0x3097A8D: "kernel32.dll.GetLastError",
    0x3097ABC: "advapi32.dll.GetTokenInformation",
    0x309B922: "advapi32.dll.GetTokenInformation",
    0x309B94E: "kernel32.dll.CloseHandle",
    0x309307A: "advapi32.dll.GetLengthSid",
    0x30980FA: "advapi32.dll.InitializeSecurityDescriptor",
    0x3098118: "advapi32.dll.SetSecurityDescriptorDacl",
    0x3094FDB: "kernel32.dll.GetVersionExA",
    0x3098161: "advapi32.dll.ConvertStringSecurityDescriptorToSecurityDescriptorW",
    0x30981F3: "advapi32.dll.GetSecurityDescriptorSacl",
    0x3098217: "advapi32.dll.SetSecurityDescriptorSacl",
    0x3095C81: "kernel32.dll.GetVersionExW",
    0x3098C0A: "advapi32.dll.OpenProcessToken",
    0x3098C37: "advapi32.dll.GetTokenInformation",
    0x3098C7A: "kernel32.dll.GetLastError",
    0x3098CE2: "advapi32.dll.GetTokenInformation",
    0x3098D0D: "advapi32.dll.GetSidSubAuthorityCount",
    0x3098D35: "advapi32.dll.GetSidSubAuthority",
    0x3091C6F: "kernel32.dll.HeapFree",
    0x3098D5C: "kernel32.dll.CloseHandle",
    0x309B18A: "shell32.dll.SHGetFolderPathW",
    0x309B1D3: "shlwapi.dll.PathAddBackslashW",
    0x309B1E6: "kernel32.dll.GetVolumeNameForVolumeMountPointW",
    0x309B210: "shlwapi.dll.PathRemoveBackslashW",
    0x309B222: "shlwapi.dll.PathRemoveFileSpecW",
    0x309B243: "shlwapi.dll.PathAddBackslashW",
    0x309B256: "kernel32.dll.GetVolumeNameForVolumeMountPointW",
    0x309B299: "ole32.dll.CLSIDFromString",
    0x30923CD: "kernel32.dll.GetCurrentProcessId",
    0x309187E: "kernel32.dll.CreateEventW",
    0x309A4F5: "ole32.dll.StringFromGUID2",
    0x309186C: "kernel32.dll.CreateEventW",
    0x3091D8B: "kernel32.dll.WaitForSingleObject",
    0x309EE85: "ntdll.dll.RtlReAllocateHeap",
    0x3096786: "kernel32.dll.IsWow64Process",
    0x309D526: "advapi32.dll.RegOpenKeyExW",
    0x3097843: "kernel32.dll.CreateMutexW",
    0x3097863: "kernel32.dll.WaitForSingleObject",
    0x30926EF: "shell32.dll.SHGetFolderPathW",
    0x30973EC: "kernel32.dll.GetComputerNameW",
    0x3097457: "kernel32.dll.GetVersionExW",
    0x309D552: "advapi32.dll.RegQueryValueExW",
    0x309D57B: "advapi32.dll.RegCloseKey",
    0x309D840: "advapi32.dll.RegOpenKeyExW",
    0x309D86D: "advapi32.dll.RegQueryValueExW",
    0x309D8DC: "advapi32.dll.RegQueryValueExW",
    0x309D898: "advapi32.dll.RegCloseKey",
    0x30957AE: "shlwapi.dll.wvnsprintfW",
    0x30A0C1B: "kernel32.dll.GetTickCount",
    0x309DCC3: "user32.dll.CharUpperW",
    0x30984A7: "kernel32.dll.Sleep",
    0x309CFA0: "shlwapi.dll.PathCombineW",
    0x309DD87: "kernel32.dll.GetFileAttributesW",
    0x3096240: "kernel32.dll.CreateDirectoryW",
    0x309DDED: "shlwapi.dll.PathAddExtensionW",
    0x30993F0: "advapi32.dll.OpenThreadToken",
    0x3099401: "kernel32.dll.GetCurrentThread",
    0x3099421: "advapi32.dll.OpenProcessToken",
    0x3099462: "advapi32.dll.LookupPrivilegeValueW",
    0x3099482: "advapi32.dll.AdjustTokenPrivileges",
    0x30994A6: "kernel32.dll.GetLastError",
    0x30994C1: "kernel32.dll.CloseHandle",
    0x30921A9: "advapi32.dll.ConvertStringSecurityDescriptorToSecurityDescriptorW",
    0x30921EF: "advapi32.dll.GetSecurityDescriptorSacl",
    0x3092219: "advapi32.dll.SetNamedSecurityInfoW",
    0x3092238: "kernel32.dll.LocalFree",
    0x309D3BD: "advapi32.dll.RegCreateKeyExW",
    0x309D42D: "advapi32.dll.RegCreateKeyExW",
    0x309D458: "advapi32.dll.RegCloseKey",
    0x309D47F: "advapi32.dll.RegCloseKey",
    0x30988A9: "kernel32.dll.WideCharToMultiByte",
    0x309E26A: "advapi32.dll.RegCreateKeyExW",
    0x309E29E: "advapi32.dll.RegSetValueExW",
    0x309E2D1: "advapi32.dll.RegCloseKey",
    0x30A0477: "kernel32.dll.CreateFileW",
    0x30A1A49: "kernel32.dll.MultiByteToWideChar",
    0x30A0647: "advapi32.dll.CryptAcquireContextA",
    0x30A0680: "advapi32.dll.CryptCreateHash",
    0x30A06B4: "advapi32.dll.CryptHashData",
    0x30A06D4: "advapi32.dll.CryptGetHashParam",
    0x30A070B: "advapi32.dll.CryptDestroyHash",
    0x30A071F: "advapi32.dll.CryptReleaseContext",
    0x309192E: "kernel32.dll.ReleaseMutex",
    0x3091941: "kernel32.dll.CloseHandle",
    0x309AB96: "advapi32.dll.RegOpenKeyExW",
    0x309ABD3: "advapi32.dll.RegQueryValueExW",
    0x309ABF5: "advapi32.dll.RegCloseKey",
    0x309843F: "kernel32.dll.CreateThread",
    0x3091EB2: "kernel32.dll.WaitForSingleObject",
    0x3091BAD: "ntdll.dll.RtlAllocateHeap",
}


add_bulk_decompiler_comments(addr_comment_dict)
