from tkinter import *
tk = Tk()
txt = Text(tk)
txt.pack()

def event_info (event):
	txt.delete("1.0", END)
	for k in dir(event):
		if k[0] != "_":
			ev = "%15s: %s\n" % (k, repr(getattr(event, k)))
			txt.insert(END, ev)
	return

txt.bind ("<KeyPress>", event_info)
tk.mainloop()