#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'chenjunsheng'

import os
import os.path
import tinify

tinify.key = "zp8XWlmqgxODG4MLB8aO2XRO3L9BZZPO"

def compress(path):

    for dir_path, dir_names, file_names in os.walk(path):
        file_names = filter(lambda file_name: file_name[-4:] == '.png', file_names)
        file_names = map(lambda file_name: os.path.join(dir_path, file_name), file_names)
        for file in file_names:
            print(file)
            source = tinify.from_file(file)
            source.to_file(file)

        file_names = filter(lambda file_name: file_name[-4:] == '.jpg', file_names)
        file_names = map(lambda file_name: os.path.join(dir_path, file_name), file_names)
        for file in file_names:
            print(file)
            source = tinify.from_file(file)
            source.to_file(file)

if __name__ == '__main__':
    # try:
    #     filenames = get_all_file_in(os.getcwd())
    #     for filename in filenames:
    #         print filename
    # except:
    #     print "execute list_file_dir fun error"
    compress(os.getcwd())
