#!/usr/bin/env python
#coding=utf8
#删除当前目录及子目录中的.svn目录

import os
import shutil

def recursive_file(dir_path):
    parents = os.listdir(dir_path)

    for parent in parents:
        child = os.path.join(dir_path, parent)
        
        if os.path.isdir(child):
            if parent == ".svn":
                print child
                shutil.rmtree(child)
            else:
                recursive_file(child)


if __name__ == '__main__':
    recursive_file(os.getcwd())

