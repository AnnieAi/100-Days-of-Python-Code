from tkinter import *
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# 控制 grid 第 1、2 列的宽度
window.grid_columnconfigure(1, minsize=260)
window.grid_columnconfigure(2, minsize=150)

# Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

# Buttons
generate_pwd = Button(text="Generate Password")
generate_pwd.grid(row=3, column=2, sticky="ew")

add = Button(text="Add")
add.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
