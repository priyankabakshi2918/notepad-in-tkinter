
from tkinter import *
from tkinter import filedialog, messagebox


root = Tk()
root.title("My Notepad")
root.geometry("800x500")

 
text_area = Text(root, font=("Arial", 14), undo=True)
text_area.pack(fill=BOTH, expand=1)


scroll = Scrollbar(text_area)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)

 
def new_file():
    text_area.delete(1.0, END)
    root.title("Untitled - Notepad")

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                       filetypes=[("Text Documents", "*.txt"),
                                                  ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(f"{file} - Notepad")
        text_area.delete(1.0, END)
        with open(file, "r") as f:
         text_area.insert(1.0, f.read())

def save_file():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                         defaultextension=".txt",
                                        filetypes=[("Text Documents", "*.txt"),
                                                   ("All Files", "*.*")])
    if file == "":
        return
    with open(file, "w") as f:
        f.write(text_area.get(1.0, END))
    messagebox.showinfo("Save", "File Saved Successfully!")

def cut_text():
   text_area.event_generate(("<<Cut>>"))

def copy_text():
   text_area.event_generate(("<<Copy>>"))

def paste_text():
    text_area.event_generate(("<<Paste>>"))

def about():
    messagebox.showinfo("About Notepad", "Simple Notepad made using Tkinter in Python")

 
menu_bar = Menu(root)
root.config(menu=menu_bar)

  
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)


edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


root.mainloop()