import asyncio
from aiopath import AsyncPath
from libcpp.vector import vector

cdef vector[] files(vector filenames, filesize: int):
    cdef vector[] target_files
