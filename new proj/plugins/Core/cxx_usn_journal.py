from ctypes import c_char, POINTER, c_ulong, c_void_p
from typing import TypeVar, TypeAlias

HANDLE: TypeAlias = c_void_p
LPCSTR = TypeVar("LPCSTR", bound=POINTER(c_char))
PCSTR = TypeVar("PCSTR", bound=POINTER(c_char))
DWORD = TypeVar("DWORD", bound=POINTER(c_ulong))
LPCVOID: TypeAlias = c_void_p

class _SECURITY_ATTRIBUTES:
    def __init__(self, nLength: DWORD, lpSecurityDescriptor: LPCVOID, bInheritHandle: bool):
        self.nLength: DWORD = nLength
        self.lpSecurityDescriptor: LPCVOID = lpSecurityDescriptor
        self.bInheritHandle: bool = bInheritHandle

SECURITY_ATTRIBUTES: TypeAlias = _SECURITY_ATTRIBUTES
PSECURITY_ATTRIBUTES: TypeAlias = POINTER(_SECURITY_ATTRIBUTES)
LPSECURITY_ATTRIBUTES: TypeAlias = POINTER(_SECURITY_ATTRIBUTES)

#def CreatFileA(lpFileName: LPCSTR, dwDesiredAccess: DWORD, dwShareMode: DWORD, lpSecurityAttributes: LPSECURITY_ATTRIBUTES, dwCreationDisposition: DWORD, dwFlagsAndAttributes: DWORD, hTampleFile: HANDLE):

