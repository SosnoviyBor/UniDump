from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

# Summoning the great evil
root = Tk()
FILE_NAME = NONE

# Creating functionality
def newFile ():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete("1.0", END)

def saveFile ():
	data = text.get('1.0', END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def saveFileAs ():
	out = asksaveasfile(mode='w', defaultextension='.txt')
	data = text.get('1.0', END)
	out.write(data)
	out.close()

def openFile ():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp == NONE:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete("1.0", END)
	text.insert("1.0", data)

def info ():
	showinfo("Info", "Made by Sosnoviy Bor")

def findText ():
	#to be added
	return

def replaceText ():
	#to be added
	return

# Customizing the main window
# window properties
root.title("Word++")
root.geometry('500x400')
# text widget
text = Text(root, wrap = WORD)
# scrollbar widget
scrollbar = Scrollbar(root, orient=VERTICAL, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
# menu widgets
menuBar = Menu(root)		# all the main buttons
menuFile = Menu(menuBar)	# the "File" button
menuEdit = Menu(menuBar)	# the "Edit" button
menuBar.add_cascade(label="File", menu=menuFile)
menuBar.add_cascade(label="Edit", menu=menuEdit)
menuBar.add_cascade(label="Info", command=info)
menuFile.add_command(label="New File", command=newFile)
menuFile.add_command(label="Open", command=openFile)
menuFile.add_command(label="Save", command=saveFile)
menuFile.add_command(label="Save as", command=saveFileAs)
menuEdit.add_command(label="Find text")
menuEdit.add_command(label="Replace text")
# Widget assignment
root.config(menu=menuBar)
scrollbar.pack(side="right", fill="y")
text.pack()

# Start of visuaization
root.mainloop()


'''
#############################################
TODO
1. Rework newFile function
2. Add findText function
3. Add replaceText function
4. Ask for saving an unsaved file before quitting (?)
#############################################
'''