from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

# Summoning the great evil
root = Tk()
FILE_NAME = NONE

# Creating functionality
# functions for "New File" menu button
def newFileCheck():
	if text.get('1.0', END).rstrip() != "":
		unsavedChanges()
	else:
		newFile()

def unsavedChanges():
	global ucWindow
	ucWindow = Toplevel(root, height=100, width=400)
	ucWindow.title("Unsaved changes")
	ucWindow.resizable(False, False)

	label = Label(ucWindow, text="Do you want to save changes to "+FILE_NAME+" ?")
	buttSaveas = Button(ucWindow, text="Save", width=10)
	buttDontSave = Button(ucWindow, text="Don't save", width=10)
	buttCancel = Button(ucWindow, text="Cancel", width=10)

	buttSaveas['command'] = combinedFunc1
	buttDontSave['command'] = combinedFunc2
	buttCancel['command'] = ucWindow.destroy

	label.pack()
	buttSaveas.pack()
	buttDontSave.pack()
	buttCancel.pack()
def combinedFunc1():
	saveFileAs()
	ucWindow.destroy()
def combinedFunc2():
	newFile()
	ucWindow.destroy()

def newFile ():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete("1.0", END)

# function for "Save" menu button
def saveFile ():
	data = text.get('1.0', END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

# function for "Save as" menu button
def saveFileAs ():
	out = asksaveasfile(mode='w', defaultextension='.txt')
	data = text.get('1.0', END)
	out.write(data)
	out.close()

# function for "Open" menu button
def openFile ():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp == NONE:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete("1.0", END)
	text.insert("1.0", data)

# funtion for "Info" menu button
def info ():
	showinfo("Info", "Made by Sosnoviy Bor")

# function for "Find text" menu button
def findText ():
	#to be added
	return

# function for "Replace text" button
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
menuFile.add_command(label="New File", command=newFileCheck)
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
1. Rework newFile function		DONE
2. Add findText function
3. Add replaceText function
4. Ask for saving an unsaved file before quitting (?)
#############################################
'''