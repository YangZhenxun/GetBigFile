import sys
import time
import asyncio
import threading
from aiopath import AsyncPath

async def files(filenames, filesize):
    target_files = []
    for filename in filenames:
        target_file = await filename.resolve()
        if not await target_file.is_file():
            continue
        size = (await target_file.stat()).st_size
        if size >= filesize*1024:
            size = f'{size}KB'
            print(target_file)
            target_files.append(target_file)
    return target_files

async def k(dir_i, filesize):
    target_files = []
    async for filename in dir_i.glob("**/*"):
        target_file = await filename.resolve()
        if not await target_file.is_file():
            continue
        size = (await target_file.stat()).st_size
        if size >= filesize*1024:
            size = f'{size}KB'
            print(target_file)
            target_files.append(target_file)
    return target_files

async def a(st_dir: AsyncPath, drs: list, flnms: list) -> tuple[list, list]:
    async for fl_ad_drs in st_dir.iterdir():
        if await fl_ad_drs.is_dir():
            drs.append(await fl_ad_drs.resolve())
        else:
            flnms.append(await fl_ad_drs.resolve())
    return drs, flnms

async def amain():
    start_dir = AsyncPath("C:/")
    dirs:list = []
    filenames:list = []
    t = asyncio.create_task(a(start_dir, dirs, filenames))
    filesize = 1024*1024

    start = time.time()
    dirs, filenames = await t
    task = [asyncio.create_task(k(dir_i, filesize)) for dir_i in dirs]
    task.append(asyncio.create_task(files(filenames, filesize)))
    all_r = await asyncio.gather(*task)
    print(all_r)
    end = time.time()
    print(end - start)

asyncio.run(amain())
