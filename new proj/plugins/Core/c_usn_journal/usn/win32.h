#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <fileapi.h>

PyObject *wrapCreateFileA(PyObject *self, PyObject *args){
    _In_ LPCSTR lpFileName;
    _In_ DWORD dwDesiredAccess;
    _In_ DWORD dwShareMode;
    _In_opt_ LPSECURITY_ATTRIBUTES lpSecurityAttributes;
    _In_ DWORD dwCreationDisposition;
    _In_ DWORD dwFlagsAndAttributes;
    _In_opt_ HANDLE hTemplateFile;
    if (!PyArg_VaParse(args, "s", lpFileName,
        dwDesiredAccess, 
        dwShareMode, 
        lpSecurityAttributes, 
        dwCreationDisposition, 
        dwFlagsAndAttributes,
        hTemplateFile))
        return NULL;
}