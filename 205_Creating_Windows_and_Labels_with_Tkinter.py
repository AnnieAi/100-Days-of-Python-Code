import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# 只是创建了一个 Label 对象，相当于“我做了一个标签”，但它还没有真正被安排到窗口里面。

my_label.pack()
# 就是告诉 tkinter：把这个 Label 塞进窗口里，并自动找个位置摆好。
# pack 这个词本身有点像“打包/塞进去”，它会按照默认规则把控件放进窗口，通常是从上往下排列；比如你有三个 label 都 .pack()，它们就会一个接一个竖着排下来。
# 你现在完全不用管什么 **kw，那只是说 .pack() 里面可以放一些可选参数

window.mainloop()