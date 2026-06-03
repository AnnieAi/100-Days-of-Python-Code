from tkinter import *

def converting():
    input_mile = float(input.get())
    km_num = input_mile * 1.60934
    Km_num.config(text=f"{km_num}")


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

Km_num = Label(text="0")
Km_num.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

## Button
Calculate = Button(text="Calculate", command=converting)
Calculate.grid(column=1, row=2)

window.mainloop()