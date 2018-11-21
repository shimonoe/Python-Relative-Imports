# Python-Relative-Imports
This is a simple tutorial for relative imports in Python 2.x/3.x

---

This example uses a function to walk through directories from project folder. You just need to pass two arguments: The name of the root folder(root_dir_name) and the name of the module(module_name) inside this folder.

```
##
# This function appends modules directories inside the project for relative imports
#
# @root_dir_name String The root directory name
# @module_name String The name of directory that contains the module
##
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
```
