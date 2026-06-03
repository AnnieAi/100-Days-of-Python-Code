from tkinter import *

def button_clicked():
    label.config(text=input.get())


# Window
window = Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

## Label
label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
label.config(padx=10, pady=20)

## Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Or Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

## Entry
input = Entry(width=30)
input.grid(column=3, row=2)



window.mainloop()


# Brief Notes
"""
这一课讨论的是Layout的内容。首先：
If a widget gets created but it doesn't have any layout specified using pack, place or grid, then it won't be shown here.

而想要做Layout的话，主要有3个Layout Manager：
1. 在前面几节接触过的pack
By default, pack will always start from top and pack every other widget just below the previous one.
You can change it by adding a side parameter.
However, pack is not easy to do precise layout.

2. place
Place is about precise positioning.
eg: input.place(x=3, y=2)

当只有少数几个widgets时，这个方法很nice，但是当有几十个上百个widgets时，这就会变得很折磨。

3. grid
把window划分成若干个column和row，然后根据格子来分配widget。


这一课在做的就是，把label，两个button，entry，在window中排列好。
"""
