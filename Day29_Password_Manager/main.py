from tkinter import *
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Windows
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=YELLOW) # widgets 会被放在离 window 内边缘 20 像素之后的区域里

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.pack()


window.mainloop()
