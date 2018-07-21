import tkinter
from tkinter import *
from tkinter import ttk
import random
import os
import sys
import tkinter.ttk as ttk
#counter (group X)
grou = 0 #Glocal value
def add_one(): #Add one to the counter when new groups are generated
    global grou #Glocal value
    grou += 1
def clear(): #Clear Textbox one, run random_class(), reset counter
    global grou #Glocal value
    grou = 0
    text_box.delete(1.0, END)
    random_class()
def clear2(): #Clear Textbox one and run getList()
    text_box2.delete(1.0, END)
    getList()
def replace(): #remove brackets
    texter = text_box.get(1.0, END)
    c = texter.replace('[','').replace(']','') #Linux'
    text_box.delete(1.0, END)
    text_box.insert(INSERT, c)
def write(self): #Insert generated list from random_class to textbox1 and add group counter
    add_one()
    number = str(grou)
    num = "Group "
    text_box.insert(INSERT, num + number +":")
    text_box.insert(INSERT, '\n')
    text_box.insert(INSERT, self)
    replace()
def randomList(a):  # function to randomize a list of students
    b = []
    for i in range(len(a)):  # get the length of the list
        item = random.choice(a)  # get random name from the list
        a.remove(item)  # remove the randomly chosen name from the original list (a)
        b.append(item)  # add the randomly chosen name to the new list (b)
    return b
def saveText(): #Save generated list to Generated(folder)
    texter = text_box.get(1.0, END)
    gen = "Generated"
    filename = e3.get()
    pathing = os.path.abspath(os.pardir)
    path = os.getcwd()
    filepath = os.path.join(path, gen)
    name = os.path.join(filepath, filename)
    target = open(name, 'w')
    target.write(texter)
    target.close()
def saveList(): #Save edited list
    textlist = text_box2.get(1.0, END)
    clas = "Class"
    filename = eb2.get()
    pathing = os.path.abspath(os.pardir)
    path = os.getcwd()
    filepath = os.path.join(path, clas)
    name = os.path.join(filepath, filename)
    target = open(name, 'w')
    target.write(textlist)
    target.close()
def getList(): #Display class list in textbox2
    textlist = text_box2.get(1.0, END)
    clas = "Class"
    filename = eb2.get()
    pathing = os.path.abspath(os.pardir)
    path = os.getcwd()
    filepath = os.path.join(path, clas)
    name = os.path.join(filepath, filename)
    target = open(name, 'r')
    temps = target.read()
    text_box2.insert(INSERT, temps)
def random_class():
    # open the text file of student data and write it to a list
    choice = os.path.join(filepath, eb1.get())
    workingClass = open(choice, 'r')
    templist = workingClass.readlines()
    stulist = []  # create an empty list that will be populated with user-chosen class list
    for student in templist:
        temp = student.rstrip('\n')  # strip the newline (\n) character from each list string
        stulist.append(temp)  # add next student from file to the list

    shuffledlist = randomList(stulist)  # randomize the list
    numstu = int(e2.get())
    while shuffledlist:  # print randomized groups for the user
        write(shuffledlist[0:numstu])
        shuffledlist[0:numstu] = []
#Group Number
# Get class list in the "Class" folder
clas = "Class"
pathing = os.path.abspath(os.pardir)  # Get path (exclude the function folder)
path = os.getcwd()  # Get path
# If launching using run.py use path, if running from Grouper.py use pathing
filepath = os.path.join(path, clas)  # join paths
# Get text file containing the class to be randomized from the user
for roots, dirs, files in os.walk(filepath):  # Find files in "Class" folder
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    break
app = Tk() #Create Window
app.title("Grouper")
main = Frame(app)
main.pack()
#resizeable grid
Grid.rowconfigure(app, 0, weight=1)
Grid.columnconfigure(app, 0, weight=1)
main.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(main)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(main, 7, weight=1)
Grid.columnconfigure(main, 0, weight=1)
#resize
for x in range(10):
  Grid.columnconfigure(main, x, weight=1)

for y in range(5):
  Grid.rowconfigure(main, y, weight=1)
#Create Labelfram for dropdown menu
ebs1 = ttk.Labelframe(main, text="Class")
ebs2 = ttk.Labelframe(main, text="Select a Class list to edit")
#Create dropdown menu in Labelframe
eb1 = ttk.Combobox(ebs1, values=files, state='readonly')
eb2 = ttk.Combobox(ebs2, values=files, state='readonly')
#Place Labelframe in Grid
eb1.pack(pady=5, padx=10)
ebs1.grid(row=0, column=0)
eb2.pack(pady=5, padx=10)
ebs2.grid(row=0, column=3)
#Create and set theme
style = ttk.Style()
style.theme_create('framestyle', parent='alt',
                        settings = {'TLabelframe':
                                    {'configure':
                                      {'selectbackground': 'white',
                                       'fieldbackground': 'white',
                                       'background': 'white',
                                       }}}
                         )
#Create label and place it in the grid
number = ttk.LabelFrame(main, text="Students per Group")
save= ttk.LabelFrame(main, text="File name")
number.grid(row=1, column=0)
save.grid(row=1, column=2)
label = Label(main, text="Enter file name and\nclick Save to save\ngenerated group list.")
label.grid(row=2, column=2)
#Create Entry box for Students per Group and Save/File name
e2 = ttk.Entry(number)
e2.pack()
e3 = ttk.Entry(save)
e3.pack()
#Create Textbox to display Text
text_box = tkinter.Text(main, state=tkinter.NORMAL, width=50, pady=5, padx=5)
text_box.grid(row=3, column=0, columnspan=2)
text_box2 = tkinter.Text(main, state=tkinter.NORMAL, width=50, pady=5, padx=5)
text_box2.grid(row=3, column=3, columnspan=2)
#Insert text into textbox.
text_box.insert(INSERT, "   ╭━━━╮\n   ┃╭━╮┃\n   ┃┃╱╰╋━┳━━┳╮╭┳━━┳━━┳━╮\n   ┃┃╭━┫╭┫╭╮┃┃┃┃╭╮┃┃━┫╭╯\n   ┃╰┻━┃┃┃╰╯┃╰╯┃╰╯┃┃━┫┃\n   ╰━━━┻╯╰━━┻━━┫╭━┻━━┻╯\n   ╱╱╱╱╱╱╱╱╱╱╱╱┃┃    Bᴏʙ\n   ╱╱╱╱╱╱╱╱╱╱╱╱╰╯\n \n   Select a class list, enter number of students \n   per group and hit generate.")
text_box2.insert(INSERT,"    Select a class list and click Load to edit.  \n    Click Save when you are done editing.")
#Create buttons and place it in grid
Button(main, text='Generate', command=clear).grid(row=0, column=1, sticky=W, pady=4)
Button(main, text='Quit', command=app.quit).grid(row=1, column=1, sticky=W, pady=4)
Button(main, text='Save', command=saveText).grid(row=0, column=2, columnspan=2, sticky=W, pady=4)
Button(main, text='Load', command=clear2).grid(row=0, column=4, sticky=W, pady=4)
Button(main, text='Save', command=saveList).grid(row=1, column=4, sticky=W, pady=4)
#Set size of the window
app.geometry("900x550")
app.mainloop()
