"""This module sorts a directory"""
import sys
import os

#collects dir name given
try:
    ARG_DIR=sys.argv[1]
except IndexError:
    print("ERROR: No Directory Given")
    sys.exit()

DIR_LIST = os.listdir(ARG_DIR)

def __make_dir__(dirs):
    ext_list = []

    #makes a dir for every type of extension
    for i in dirs:
        ext = i.split(".")
        try:
            ext_list.append(ext[1])
        except IndexError:
            continue

    ext_list = set(ext_list)
    counter = 0
    for i in ext_list:
        try:
            os.mkdir(ARG_DIR + i)
            print("New dir made named: " + i)
            counter += 1
        except FileExistsError:
            continue
    return str(counter) + " Dir's made."
print(__make_dir__(DIR_LIST))
