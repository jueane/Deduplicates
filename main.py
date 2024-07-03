#!venv/bin/python

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import hashlib
import sys


def get_file_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def find_duplicates(dir1, dir2):
    files_md5 = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(dir1):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_md5 = get_file_md5(file_path)
            files_md5[file_md5] = file_path

    for dirpath, _, filenames in os.walk(dir2):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_md5 = get_file_md5(file_path)
            if file_md5 in files_md5:
                duplicates.append(file_path)

    return duplicates


def delete_files(file_list):
    for file_path in file_list:
        os.remove(file_path)
        print(f"Deleted: {file_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir1 = "/jdata/dockerData/books"
    dir2 = "/jdata/dockerData/GoogleDriveBooks"

    duplicates = find_duplicates(dir1, dir2)
    delete_files(duplicates)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
