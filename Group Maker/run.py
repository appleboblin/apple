# Group Maker
# To run, make sure Python3 and tkinter package is installed, change directory to program folder, then type "python3 run.py" at the command line
'''
Group maker requires text files of students, one student per line in the "Class" folder.
Additional functions:
    Edit class list
    Save generated group list
Future ideas/functions:
    Object Oriented
    Create class lsit
    Better gui. With Notebook
    Separate files for separate functions
'''

try:
    from function import Grouper
except ImportError:
    import sys
    import os
    folder = "function"
    path = os.getcwd()
    filepath = os.path.join(path, folder)
    sys.path.insert(0, filepath)
    import Grouper
