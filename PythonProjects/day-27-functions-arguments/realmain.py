from tkinter import *


# For Window Set Up
window = Tk()
window.title('My First GUI Program')
window.minsize(width=500,height=300)

# Label

my_label = Label(text='Hi Baby')
my_label.pack()

# Input
input = Entry()
input.pack()


# Button
def button_clicked():
    name = input.get()
    my_label.config(text=f'Name :{name}')
    print(name)
button = Button(text='Click Me', command=button_clicked)
button.pack()


window.mainloop()