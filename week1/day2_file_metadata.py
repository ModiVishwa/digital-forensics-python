import os
import time

filename = input("Enter filename to analyze: ")

if os.path.exists(filename):
    stats = os.stat(filename)

    print(f" File: {filename}")
    print(f" Size: {stats.st_size}")
    print(f" Created: {time.ctime(stats.st_ctime)}")
    print(f" Modified: {time.ctime(stats.st_mtime)}")
    print(f" Accessed: {time.ctime(stats.st_atime)}")

else:
    print("File Not Found.")