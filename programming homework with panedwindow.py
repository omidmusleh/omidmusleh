from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("680x400")
win.title("Application For Programming Home Works")
win.resizable(width=False,height=False)
pan_1 = PanedWindow(win,bg="lightblue",bd=4,orient=HORIZONTAL)
pan_1.pack(expand=True,fill=BOTH)
# pan_2 = PanedWindow(bg="green")
# pan_1.add(pan_2)
pan_4 = PanedWindow(bg="lightblue",orient=VERTICAL)
pan_1.add(pan_4)
def first_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\PREMIER OMPUTER\Desktop\\PycharmProjects\\programming homework\\built-in function.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
def second_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\PREMIER OMPUTER\\Desktop\\PycharmProjects\\programming homework\\factorial and fibonanci.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
def third_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\PREMIER OMPUTER\\Desktop\\PycharmProjects\\programming homework\\honai.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
# content = StringVar()
lab = Label(text="HOMEWORKS",bg="lightblue")
pan_4.add(lab)
first = Button(text="Built-in function",width=12,height=3,command=first_work)
pan_4.add(first)
second = Button(text="factorial",width=12,height=3,command=second_work)
pan_4.add(second)
third = Button(text="Hanoi tower",width=12,height=3,command=third_work)
pan_4.add(third)
def my_text(*args):
    my_text.yview(*args)
def Exit():
    ex = messagebox.askquestion("Exit","do you want to Exit")
    if ex == "yes":
        win.quit()
btn4 = Button(text="Exit",width=12,height=3,command=Exit)

def fourth_work():
    my_text.delete(1.0, END)
    with open("C:\\Users\\PREMIER OMPUTER\\Desktop\\PycharmProjects\\programming homework\\oop homework.txt", "r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
btn_5 = Button(text="OOP Exercises",height=3,command=fourth_work)
pan_4.add(btn_5)
pan_4.add(btn4)
pan_text = PanedWindow(bg="lightblue",bd=2)
pan_1.add(pan_text)
scroll = Scrollbar(pan_1)
# scroll.pack(side=RIGHT,fill=BOTH)
my_text = Text(width=70,height=25,yscrollcommand=scroll.set)
scroll.config(command=my_text.yview)
pan_text.add(my_text)
pan_1.add(scroll)
win.mainloop()
