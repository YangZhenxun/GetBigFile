cimport c_usn_journal
from libc.stddef cimport wchar_t
from libc.stdint cimport int64_t

def CreateFile(lpFileName,dwDesiredAccess,dwShareMode,                   \
        lpSecurityAttributes,dwCreationDisposition,dwFlagsAndAttributes, \
        hTemplateFile):
    cdef void *chTemplateFile
    cdef c_usn_journal.LPSECURITY_ATTRIBUTES c_lp_sa
    chTemplateFile = <void *>hTemplateFile
    c_lp_sa = <c_usn_journal.LPSECURITY_ATTRIBUTES>lpSecurityAttributes
    cdef c_usn_journal.HANDLE ccreate = c_usn_journal.CreateFileA(lpFileName,dwDesiredAccess,dwShareMode, \
        c_lp_sa,dwCreationDisposition,dwFlagsAndAttributes,                                               \
        chTemplateFile)
    return <object>ccreate

def GetVolumeInformation(lpRootPathName,lpVolumeNameBuffer,            \
        nVolumeNameSize,lpVolumeSerialNumber,lpMaximumComponentLength, \
        lpFileSystemFlags, lpFileSystemNameBuffer,nFileSystemNameSize):
    cdef bint cget = c_usn_journal.GetVolumeInformationW(<c_usn_journal.LPCWSTR>lpRootPathName,<c_usn_journal.LPWSTR>lpVolumeNameBuffer,\
        nVolumeNameSize,<c_usn_journal.LPDWORD>lpVolumeNameBuffer,<c_usn_journal.LPDWORD>lpMaximumComponentLength,                                     \
        <c_usn_journal.LPDWORD>lpFileSystemFlags, <c_usn_journal.LPWSTR>lpFileSystemNameBuffer,nFileSystemNameSize)
    return <object>cget
