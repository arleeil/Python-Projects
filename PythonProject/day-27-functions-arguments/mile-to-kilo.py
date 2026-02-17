from tkinter import *
import math

# Screen
window = Tk()
window.minsize(height=300, width=500)
window.title('Calculator')
window.config(padx=200, pady=100)



is_equal = Label(text='is equal to')
is_equal.grid(column=1,row=2)

label1 = Label(text='Miles')
label1.grid(column=3,row=1)

label2 = Label(text='Km')
label2.grid(column=3,row=2)

label3 = Label(text='0')
label3.grid(column=2,row=2)

user_miles = Entry(width=7)
user_miles.grid(column=2,row=1)

def calculate():
    num = user_miles.get()
    kilometers = int(num) * 1.60934
    label3.config(text=math.ceil(kilometers))
button = Button(text='Calculate', command=calculate)
button.grid(column=2,row=3)


window.mainloop()