from tkinter import *

def converting():
    input_mile = float(input.get())
    km_num = input_mile * 1.60934
    return km_num

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

## Entry
input = Entry()
input.grid(column=1, row=0)

## Labels
mile = Label(text="Miles")
mile.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

Km_num = Label(text=converting())
Km_num.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

## Button
Calculate = Button(text="Calculate", command=converting)
Calculate.grid(column=1, row=2)

window.mainloop()

"""
报错：
Traceback (most recent call last):
  File "D:\1CodingSpace\Python\Python100\Day27_GUI_Program_Beginner\212_Mile_to_Kilometers_Converter_Project.py", line 25, in <module>
    Km_num = Label(text=converting())
                        ^^^^^^^^^^^^
  File "D:\1CodingSpace\Python\Python100\Day27_GUI_Program_Beginner\212_Mile_to_Kilometers_Converter_Project.py", line 4, in converting
    input_mile = int(input.get())
                 ^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''

原因：你在程序一启动的时候就写了这句：

Km_num = Label(text=converting())

这会导致 Python 立刻执行 converting()，可是这时候输入框还是空的，input.get() 得到的是空字符串 ""，然后你让它做：

int("")

所以它崩了，报错就是：空字符串不能转成整数。
"""