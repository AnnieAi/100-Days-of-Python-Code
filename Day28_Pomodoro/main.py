from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label1
timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)     # 这里的 bg=YELLOW 是在设置 Canvas 这块画布本身的背景颜色，也就是说，如果画布上什么都没有，它就是一整块黄色区域。
tomato_img = PhotoImage(file="tomato.png")  # PhotoImage(...) 会把图片文件变成 Tkinter 能使用的图片对象（PhotoImage对象）
canvas.create_image(100, 112, image=tomato_img) # 是在这块黄色画布的坐标 (100, 112) 放上番茄图片。番茄图片本身有自己的像素颜色，所以它会覆盖画布对应区域；如果 tomato.png 的背景是透明的，那么透明部分会露出下面的黄色 Canvas 背景，如果图片背景不是透明的，那图片自己的背景颜色就会盖住 Canvas。
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Button1
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

# Button2
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Label2
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
