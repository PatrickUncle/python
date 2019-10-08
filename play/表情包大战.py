import tkinter as tk
import tkinter.filedialog
from PIL import Image,ImageTk

window = tk.Tk()
def xz():
    filename = tkinter.filedialog.askdirectory()
    text.config(text = filename)


window.title("表情包大战")
window.geometry('500x300')

load = Image.open(r"E:\images\@完这群狗日的就跑，真特么刺激！狗日的来追我啊！.gif")
render = ImageTk.PhotoImage(load)

text = tk.Label(window,text='',image=render)
text.pack()

button = tk.Button(window,text="文件目录选择",command=xz)
button.pack()
window.mainloop()