import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# 创建Tkinter窗口
root = tk.Tk()
root.withdraw()  # 隐藏Tkinter窗口

# 创建一个新的顶级窗口，并设置标题
top = tk.Toplevel(root)
top.title("选择一个app")
top.withdraw()  # 隐藏新的顶级窗口

# 让用户选择一个.app文件
app_path = filedialog.askopenfilename(parent=top, title="选择一个app", filetypes=[('app files', '*.app')])

# 如果用户没有选择任何文件，显示一个错误消息并退出程序
if not app_path:
    messagebox.showerror("错误", "你没有选择任何app。")
    root.destroy()  # 退出程序
else:
    # 执行xattr命令
    subprocess.run(["xattr", "-cr", app_path])
    # 显示一个消息框，显示添加权限完成的信息
    messagebox.showinfo("信息", f"xattr操作完成，已添加权限给：{os.path.basename(app_path)}。")
    root.destroy()  # 退出程序