from tkinter import *
from tkinter.filedialog import *

tk = Tk()
tk.title("Menu")
tk.geometry("800x900")

def openfile():
	faylname = askopenfilename()
def newfile():
	pass
def savefile():
	faylname = asksaveasfilename()
Menyu = Menu()
tk.config(menu=Menyu)

fayl = Menu(Menyu,tearoff=0)
fayl.add_cascade(label="Open file",command=openfile)
fayl.add_cascade(label="New file",command=newfile)
fayl.add_cascade(label="Save",command=savefile)
fayl.add_separator()
fayl.add_cascade(label="Exit",command=tk.destroy)

edit = Menu(Menyu,tearoff=0)
edit.add_cascade(label="Cut")
edit.add_cascade(label="Copy")
edit.add_cascade(label="Past")

Menyu.add_cascade(label="File",menu=fayl)
Menyu.add_cascade(label="Edit",menu=edit)

tk.mainloop()
