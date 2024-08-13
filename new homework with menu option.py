from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

win = Tk()
win.geometry("500x400")
win.title("programming homework")
yscroll = Scrollbar(win)
yscroll.pack(side=RIGHT,fill=Y)
def text_scroll(*args):
    my_text.yview(*args)
my_text = Text(win,yscrollcommand=yscroll.set,wrap="none")
my_text.pack(expand=True,fill=BOTH)
def open_file():
    win.filename = filedialog.askopenfilename(title="select homework")
    if win.filename != '':
        with open(win.filename,"r") as f:
            my_text.delete(1.0,END)
            data = f.read()
            my_text.insert(INSERT,data)


menu_ber = Menu(win)
win.config(menu=menu_ber)
file_menu = Menu(menu_ber,tearoff=False)
menu_ber.add_cascade(menu=file_menu,label="File")
file_menu.add_command(label="Open",command=open_file)
p = len(my_text.get(1.0,END))
def save_file():
    if p != len(my_text.get(1.0,END)):
        win.filename = filedialog.asksaveasfilename()
        if ".txt" not in win.filename:
            with open(win.filename + ".txt","w") as f:
                data = my_text.get(1.0,END)
                f.write(data)
file_menu.add_command(label="Save",command=save_file)
def Exit():
    me_ex = messagebox.askyesno("Exit message","Do you want to exit")
    if me_ex == True:
        win.quit()


file_menu.add_command(label="Exit",command=Exit)
yscroll.config(command=my_text.yview)
win.mainloop()