__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Feedback mag in het Nederlands
# modules import

from os.path import abspath, exists, isdir, isfile, join
from os import mkdir, listdir
import os
from shutil import rmtree
from zipfile import ZipFile


# 1 Clean Cache

def clean_cache():

    CACHE = abspath('files/cache')

    if exists(CACHE) and isdir(CACHE):
        try:
            rmtree(CACHE)
        except OSError:
            print(f'Unable to delete directory: {CACHE}')

    try:
        mkdir(CACHE)
        if exists(CACHE) and isdir(CACHE):
            return CACHE  # cache path string
        return ''  # empty string
    except OSError:
        print(f'Unable to make directory: {CACHE}')

# 2 Cache Zip

def cache_zip(zip_path, cache_path):
    if exists(zip_path) and isfile(zip_path):
        clean_cache()
        if exists(cache_path) and isdir(cache_path):
            with ZipFile(zip_path, 'r') as myzip:
                myzip.extractall(cache_path)
            return True
    return False

# 3 Cached files

def cached_files():
    folder_name = 'cache'

    folder_path = os.path.abspath(folder_name)

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.abspath(file)
        file.replace(file, file_path)
    
    return files


print(cached_files())




