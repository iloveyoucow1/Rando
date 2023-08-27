#!/usr/bin/python
import sys
import os

directory = sys.argv[1]

dir_list = os.listdir(directory)
print(dir_list)

for i in dir_list:
    test = i.split(".")
    if test[1] == "jpg":
        os.mkdir(directory + test[1])



try:
    directory_name=sys.argv[1]
except:
    print('Please pass directory_name') 