from tkinter import *
root = Tk()		# Окно, или корень всех проблем

def str_to_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ' '.join(s)

# Первым аргументом всегда указывается мастер-виджет, на который этот конструктор будет ориентироваться
ent = Entry(root, width = 20)
but = Button(root, text = "Преобразовать")
lab = Label(root, width = 20, bg = "black", fg = "white")

but.bind('<Button-1>', str_to_sort_list)

ent.pack()
lab.pack()
but.pack()
root.mainloop()