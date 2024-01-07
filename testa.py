import multitasking
import os
import sys


dirs:list = []
filenames:list = []
start_dir:str = "C:\\"
for files_and_dirs in os.listdir(start_dir):
    if os.path.isdir(os.path.join(start_dir, files_and_dirs)):
        dirs.append(files_and_dirs)
    else:
        filenames.append(files_and_dirs)
filesize = 1024*1024

multitasking.set_max_threads(len(dirs)+1)

@multitasking.task
def k(dir_i: str):
    for dirpath, dirname, filenames in os.walk(os.path.join(start_dir, dir_i)):
        for filename in filenames:
                target_file = os.path.join(dirpath, filename)
                if not os.path.isfile(target_file):
                    continue
                size = os.path.getsize(target_file)
                size = size//1024
                if size >= filesize:
                    size = '{size}KB'.format(size=size)
                    print(target_file)

print(dirs)

for dir_i in dirs:
    k(dir_i)
for filename in filenames:
    target_file = os.path.join(start_dir, filename)
    if not os.path.isfile(target_file):
        continue
    size = os.path.getsize(target_file)
    size = size//1024
    if size >= filesize:
        size = '{size}KB'.format(size=size)
        print(target_file)
