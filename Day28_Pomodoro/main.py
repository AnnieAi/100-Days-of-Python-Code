from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None # step 2.1

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps

    # 停止倒数动作
    window.after_cancel(timer)  # after_cancel传参传的是item ID
    # 显示的时间归 00:00
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    # 修改title回"Timer"
    title_label.config(text="Timer")
    # 清除所有的checkmarks
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """1. 决定到底进入哪个工作模式：reps的逻辑
       2. 根据不同的工作模式修改UI上的title"""
    global reps     # 如果不写这一句，会报错：UnboundLocalError: cannot access local variable 'reps' where it is not associated with a value
    reps +=1        # 一进来就增加reps的值
    print(reps)     # DEBUG

    # 对不同的工作/休息模式设置不同的计时时长
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    # 选择进入不同的工作模式
    ### If it's the 1st/3rd/5th/7th reps
    if reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    ### If it's the 8th rep:
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    ### If it's 2nd/4th/6th rep:
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """1. 执行实际的倒计时操作
       2. UI修改：checkmarks增加"""
    global reps

    # 分钟数和秒数的计算，并完成显示
    count_min = math.floor(count / 60)
    count_sec = count % 60

    ### 让小于10的秒数显示09 08 07...而不是9 8 7
    if count_sec < 10:
        # count_sec = "0" + str(count_sec)
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # 递归逻辑 和 修改UI上的checkmarks
    if count > 0:  # count = 0时，停止递归（使用递归时需要设置终止语句）
        global timer    # step 2.2
        timer = window.after(1000, count_down, count - 1)  # 1000 毫秒后，调用 count_down(count - 1)      # 赋值给timer是因为reset的需求(step 1) 我猜这个timer是得到了一个item ID
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label1
title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)     # 这里的 bg=YELLOW 是在设置 Canvas 这块画布本身的背景颜色，也就是说，如果画布上什么都没有，它就是一整块黄色区域。
tomato_img = PhotoImage(file="tomato.png")  # PhotoImage(...) 会把图片文件变成 Tkinter 能使用的图片对象（PhotoImage对象）
canvas.create_image(100, 112, image=tomato_img) # 是在这块黄色画布的坐标 (100, 112) 放上番茄图片。番茄图片本身有自己的像素颜色，所以它会覆盖画布对应区域；如果 tomato.png 的背景是透明的，那么透明部分会露出下面的黄色 Canvas 背景，如果图片背景不是透明的，那图片自己的背景颜色就会盖住 Canvas。
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Button1
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Button2
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label2
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
