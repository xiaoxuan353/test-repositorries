import random
import tkinter as tk
from tkinter import messagebox

# 生成敌人选择
def other_input():
    return random.randint(1, 3)  # 1=石头, 2=剪刀, 3=布

# 判断胜负
def judgment(my_decision, enemy):
    number = my_decision - enemy
    if number == -1 or number == 2:
        return 1  # 胜利
    elif number == 1 or number == -2:
        return 0  # 失败
    else:
        return -1  # 平局

# 按钮点击事件
def on_click(button_text):
    enemy = other_input()

    # 获取用户选择
    if button_text == "石头":
        my_decision = 1
    elif button_text == "剪刀":
        my_decision = 2
    elif button_text == "布":
        my_decision = 3

    # 判断胜负
    result = judgment(my_decision, enemy)

    # 更新界面
    if result == 1:
        result_label.config(text="你赢了")
        messagebox.showinfo("恭喜你", "你赢了！")
        root.after(3000, root.quit)  # 2秒后退出程序
    elif result == 0:
        result_label.config(text="你输了或平局, 请再试一次")
    else:
        result_label.config(text="平局, 请再试一次")

# 创建主窗口
root = tk.Tk()
root.geometry("300x200")
root.title("石头剪刀布游戏")

# 创建标签用来显示结果
result_label = tk.Label(root, text="请选择 石头、剪刀 或 布")
result_label.pack(pady=10)

# 创建按钮
button1 = tk.Button(root, text="石头", command=lambda: on_click("石头"))
button1.pack(side="left", padx=10, pady=10)

button2 = tk.Button(root, text="剪刀", command=lambda: on_click("剪刀"))
button2.pack(side="left", padx=10, pady=10)

button3 = tk.Button(root, text="布", command=lambda: on_click("布"))
button3.pack(side="left", padx=10, pady=10)

# 运行主循环
root.mainloop()
