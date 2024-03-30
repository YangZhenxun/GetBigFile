from pathlib import *
import multitasking
import threading
import sys
import time

start_dir = Path("C:/")
dirs:list = []
filenames:list = []
def ff():
    global dirs, filenames
    for files_and_dirs in start_dir.iterdir():
        if Path.is_dir(files_and_dirs.resolve()):
            dirs.append(files_and_dirs.resolve())
        else:
            filenames.append(files_and_dirs.resolve())
filesize = 1024*1024
tf = threading.Thread(target=ff)
tf.start()

multitasking.set_max_threads(len(dirs)+100)

tf.join()
@multitasking.task
def k(dir_i):
    for filename in dir_i.rglob("**/*"):
        target_file = filename.resolve()
        if not Path.is_file(target_file):
            continue
        size = target_file.stat().st_size
        size = size//1024
        if size >= filesize:
            size = f'{size}KB'
            print(target_file)

def fn():
    for filename in filenames:
        target_file = filename.resolve()
        if not Path.is_file(target_file):
            continue
        size = target_file.stat().st_size
        size = size//1024
        if size >= filesize:
            size = f'{size}KB'
            print(target_file)

start = time.time()
for dir_i in dirs:
    k(dir_i)
t = threading.Thread(target=fn)
t.start()
end = time.time()
print(end - start)
