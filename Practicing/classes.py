from tkinter import *

class Block:
	def __init__ (self, master):
		self.entry1 = Entry(master, width=20)
		self.entry2 = Entry(master, width=20)
		self.button1 = Button(master, text = "+", width=10)
		self.button2 = Button(master, text = "-", width=10)
		self.button3 = Button(master, text = "*", width=10)
		self.button4 = Button(master, text = "/", width=10)
		self.label = Label(master, width=20, bg="white", fg="black")

		self.button1['command'] = self.fadd
		self.button2['command'] = self.fsub
		self.button3['command'] = self.fmult
		self.button4['command'] = self.fdiv

		self.entry1.pack()
		self.entry2.pack()
		self.button1.pack()
		self.button2.pack()
		self.button3.pack()
		self.button4.pack()
		self.label.pack()

	def fadd (self):
		result = float(self.entry1.get()) + float(self.entry2.get())
		self.label['text'] = result
	def fsub (self):
		result = float(self.entry1.get()) - float(self.entry2.get())
		self.label['text'] = result
	def fmult (self):
		result = float(self.entry1.get()) * float(self.entry2.get())
		self.label['text'] = result
	def fdiv (self):
		result = float(self.entry1.get()) / float(self.entry2.get())
		self.label['text'] = result

root = Tk()

block = Block(root)

root.mainloop()