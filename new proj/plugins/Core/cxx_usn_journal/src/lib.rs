#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]

extern crate libc;
use std::os::raw::c_void;

use pyo3::prelude::*;

use libc::{c_char, c_ulong};

pub type HANDLE = *mut c_void;
pub type LPCSTR = *const c_char;
pub type PCSTR = *const c_char;
pub type DWORD = *const c_ulong;
pub type LPVOID = *mut c_void;

#[repr(C)]
pub struct _SECURITY_ATTRIBUTES {
    pub nLength: DWORD,
    pub lpSecurityDescriptor: LPVOID,
    pub bInheritHandle: bool,
} 
pub type SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES;
pub type PSECURITY_ATTRIBUTES = *mut _SECURITY_ATTRIBUTES;
pub type LPSECURITY_ATTRIBUTES = *mut _SECURITY_ATTRIBUTES;


extern {
    pub fn _CreateFileA(
        lpFileName: LPCSTR,
        dwDesiredAccess: DWORD,
        dwShareMode: DWORD,
        lpSecurityAttributes: LPSECURITY_ATTRIBUTES,
        dwCreationDisposition: DWORD,
        dwFlagsAndAttributes: DWORD,
        hTemplateFile: LPCSTR,
    ) -> HANDLE;
}

#[pyfunction]
pub fn CreateFileA(
    lpFileName: LPCSTR,
    dwDesiredAccess: DWORD,
    dwShareMode: DWORD,
    lpSecurityAttributes: LPSECURITY_ATTRIBUTES,
    dwCreationDisposition: DWORD,
    dwFlagsAndAttributes: DWORD,
    hTemplateFile: LPCSTR,
) -> PyResult<HANDLE>
{
    unsafe{
        Ok(_CreateFileA(lpFileName, dwDesiredAccess, dwShareMode, lpSecurityAttributes, dwCreationDisposition, dwFlagsAndAttributes, hTemplateFile))    
    }
}