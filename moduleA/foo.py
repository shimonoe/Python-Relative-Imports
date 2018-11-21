# -*- coding:utf-8 -*-

import sys
import os

# Function to add relative module path to Python modules list
def import_relative(root_dir_name, module_name):
    # Find the root folder
    rpath = None
    parent_walk = os.path.realpath(__file__)
    while rpath is None:
        parent = os.path.abspath(os.path.join(parent_walk, os.pardir))
        if parent.rpartition('/')[2] != root_dir_name:
            parent_walk = parent.rpartition('/')[0]
        else:
            rpath = parent

    # Append root path to Python modules list
    if rpath not in sys.path:
        sys.path.append(rpath)

    # Append module path to Python modules list
    path_to_module = [dir for dir in os.walk(rpath) if module_name in dir[0]][0][0]
    walk_to_module = path_to_module.partition(rpath)[2].split('/')

    for path in walk_to_module:
        rel_path = rpath + '/' + path
        if rel_path not in sys.path:
            sys.path.append(rel_path)

import_relative(root_dir_name="Python-Relative-Imports-Tutorial", module_name="moduleB")

from moduleB.bar import functionB
from moduleB.moduleC.bar import functionC as functionC1
from moduleC.bar import functionC as functionC2
from moduleD.submodule.bar import functionD

if __name__ == "__main__":
    functionB()
    functionC1()
    functionC2()
    functionD()
