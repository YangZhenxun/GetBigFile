from libc.stddef cimport wchar_t
cdef extern from "<windows.h>":
    ctypedef wchar_t WCHAR
    ctypedef void *LPVOID
    ctypedef WCHAR *NWPSTR
    ctypedef WCHAR *LPWSTR
    ctypedef WCHAR *PWSTR
    ctypedef void *HANDLE
    ctypedef const WCHAR *LPCWSTR
    ctypedef unsigned long DWORD
    ctypedef DWORD *PDWORD
    ctypedef DWORD *LPDWORD
    ctypedef char CHAR
    ctypedef const CHAR *LPCSTR
    ctypedef const CHAR *PCSTR
    ctypedef struct _SECURITY_ATTRIBUTES:
        DWORD nLength
        LPVOID lpSecurityDescriptor
        bint bInheritHandle
    ctypedef _SECURITY_ATTRIBUTES SECURITY_ATTRIBUTES
    ctypedef _SECURITY_ATTRIBUTES *PSECURITY_ATTRIBUTES
    ctypedef _SECURITY_ATTRIBUTES *LPSECURITY_ATTRIBUTES

cdef extern from "<fileapi.h>":
    cdef HANDLE CreateFileA(
        LPCSTR lpFileName,                          \
        DWORD dwDesiredAccess,                      \
        DWORD dwShareMode,                          \
        LPSECURITY_ATTRIBUTES lpSecurityAttributes, \
        DWORD dwCreationDisposition,                \
        DWORD dwFlagsAndAttributes,                 \
        HANDLE hTemplateFile                        \
    )
    cdef bint GetVolumeInformationW(        \
        LPCWSTR lpRootPathName,             \
        LPWSTR lpVolumeNameBuffer,          \
        DWORD nVolumeNameSize,              \
        LPDWORD lpVolumeSerialNumber,       \
        LPDWORD lpMaximumComponentLength,   \
        LPDWORD lpFileSystemFlags,          \
        LPWSTR lpFileSystemNameBuffer,      \
        DWORD nFileSystemNameSize)
