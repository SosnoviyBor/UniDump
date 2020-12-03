from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

# Summoning the great evil
root = Tk()
FILE_NAME = NONE

# Creating functionality
# functions for "New File" menu button
def newFile():
	if text.get('1.0', END).rstrip() != "":
		unsavedChanges("newFile")
	else:
		newFileHelper()
def newFileHelper ():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete("1.0", END)

def unsavedChanges(callFrom):
	global ucWindow
	ucWindow = Toplevel(root, height=100, width=100)
	ucWindow.title("Unsaved changes")
	ucWindow.resizable(False, False)

	UCW_label = Label(ucWindow, text="Do you want to save changes to "+FILE_NAME+" ?", width=40)
	UCW_buttSaveas = Button(ucWindow, text="Save", width=10)
	UCW_buttDontSave = Button(ucWindow, text="Don't save", width=10)
	UCW_buttCancel = Button(ucWindow, text="Cancel", width=10)

	UCW_buttSaveas['command'] = unsavedChangesHelper1
	if callFrom=="newFile":
		UCW_buttDontSave['command'] = unsavedChangesHelper2
	elif callFrom == "onClosing":
		UCW_buttDontSave['command'] = unsavedChangesHelper3
	UCW_buttCancel['command'] = ucWindow.destroy

	UCW_label.pack()
	UCW_buttSaveas.pack()
	UCW_buttDontSave.pack()
	UCW_buttCancel.pack()
def unsavedChangesHelper1():
	ucWindow.destroy()
	saveFileAs()
def unsavedChangesHelper2():
	ucWindow.destroy()
	newFileHelper()
def unsavedChangesHelper3():
	ucWindow.destroy()
	root.destroy()

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
	global FTW_entryText
	FTW_entryText = StringVar()

	ftWindow = Toplevel(root, height=100, width=400)
	ftWindow.title("Find text")
	ftWindow.resizable(False, False)

	FTW_entry = Entry(ftWindow, textvariable=FTW_entryText, width=50)
	FTW_button = Button(ftWindow, text="Find next", width=10, command=findTextHelper)

	FTW_entry.pack()
	FTW_button.pack()
def findTextHelper():
	text.tag_remove('found', '1.0', END)  
	s = FTW_entryText.get()
	if s:
		idx = '1.0'
		while True:
			idx = text.search(s, idx, nocase=1,stopindex=END)
			if not idx: break
			lastidx = '%s+%dc' % (idx, len(s))
			text.tag_add('found', idx, lastidx)
			idx = lastidx
		text.tag_config('found', background='yellow')

# function for "Replace text" button
def replaceText ():
	global RTW_entry1Text
	global RTW_entry2Text
	RTW_entry1Text = StringVar()
	RTW_entry2Text = StringVar()

	global rtWindow
	rtWindow = Toplevel(root, height=100, width=400)
	rtWindow.title("Replace text")
	rtWindow.resizable(False, False)

	global RTW_entry1
	global RTW_entry2
	RTW_entry1 = Entry(rtWindow, textvariable=RTW_entry1Text, width=50)
	RTW_entry2 = Entry(rtWindow, textvariable=RTW_entry2Text, width=50)
	label1 = Label(rtWindow, text="From:")
	label2 = Label(rtWindow, text="To:")
	button = Button(rtWindow, text="Replace", width=10, command=replaceTextHelper)

	label1.pack()
	RTW_entry1.pack()
	label2.pack()
	RTW_entry2.pack()
	button.pack()
def replaceTextHelper ():
	replacedText = text.get('1.0', END).replace(RTW_entry1.get(), RTW_entry2.get())
	text.delete('1.0', END)
	text.insert('1.0', replacedText)

# function checking do you have unsaved changes
def onClosing ():
	if text.get('1.0', END).rstrip() != "":
		unsavedChanges("onClosing")
	else:
		root.destroy()

# Additional functions for lab work
#comparing amount of letter A and B
def task7 ():
	amountOfA = 0
	amountOfB = 0
	for letter in text.get('1.0', END):
		if letter == "a":
			amountOfA += 1
		elif letter == "b":
			amountOfB += 1
	if amountOfA > amountOfB:
		result = "True"
	else:
		result = "False"
	text.insert('1.0', result+"\n")

#converting int to ternary number
def task20 ():
	try:
		n = int(text.get('1.0', END))
	except:
		text.insert('1.0', showerror("Wrong argument", "I demand integer"))
		return
	text.delete('1.0', END)
	for i in range(0, n+1):
		text.insert('1.0', "Iteration #"+str(i)+": "+str(task20Helper(i))+"\n")
def task20Helper (n):
	if n == 0:
		return '0'
	nums = []
	while n:
		n, r = divmod(n, 3)
		nums.append(str(r))
	return ''.join(reversed(nums))

#uppercasing all the A letters
def task31():
	outputText = ""
	for letter in text.get('1.0', END):
		if letter == "a":
				letter = letter.upper()
		outputText += letter
	text.delete('1.0', END)
	text.insert('1.0', outputText)

# Customizing the main window
# window properties
root.title("Word++")
root.geometry('500x400')
# text widget
text = Text(root, wrap = WORD, height=2000, width=4000)
# scrollbar widget
scrollbar = Scrollbar(root, orient=VERTICAL, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
# menu widgets
menuBar = Menu(root)		# all the main buttons
menuFile = Menu(menuBar)	# the "File" button
menuEdit = Menu(menuBar)	# the "Edit" button
menuTasks = Menu(menuBar)
menuBar.add_cascade(label="File", menu=menuFile)
menuBar.add_cascade(label="Edit", menu=menuEdit)
menuBar.add_cascade(label="Info", command=info)
menuBar.add_cascade(label="Tasks", menu=menuTasks)
menuFile.add_command(label="New File", command=newFile)
menuFile.add_command(label="Open", command=openFile)
menuFile.add_command(label="Save", command=saveFile)
menuFile.add_command(label="Save as", command=saveFileAs)
menuEdit.add_command(label="Find text", command=findText)
menuEdit.add_command(label="Replace text", command=replaceText)
menuTasks.add_command(label="#7", command=task7)
menuTasks.add_command(label="#20", command=task20)
menuTasks.add_command(label="#31", command=task31)
# Widget assignment
root.config(menu=menuBar)
scrollbar.pack(side="right", fill="y")
text.pack()

# Let's add some keybindings
root.bind("<Control-o>", openFile)
root.bind("<Control-s>", saveFile)
root.bind("<Control-S>", saveFileAs)
root.bind("<Control-f>", findText)
root.bind("<Control-r>", replaceText)
root.bind("<F1>", info)

# Start of visuaization
root.protocol("WM_DELETE_WINDOW", onClosing)
root.mainloop()