import socket
import json
import tkinter as tk
import threading
import time

host = '127.0.0.1'  # 服务器的ip
port = 8080
bufsize = 1024  # 定义缓冲

username = ""

addr = (host,port)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建socket客户端


class register:


    def __init__(self):

        self.root = tk.Tk()
        self.root.title = "用户注册"
        self.root.geometry('450x300')
        tk.Label(self.root, text='用户名:').place(x=120, y=100)
        tk.Label(self.root, text='密码:').place(x=120, y=150)
        # 用户名输入框
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self.root, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=180, y=100)
        # 密码输入框
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.root, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=180, y=150)
        self.bt_login = tk.Button(self.root, text='立即注册', command=self.register)
        self.bt_login.place(x=280, y=180)
        self.root.mainloop()

    def register(self):

        global username
        # 输入框获取用户名密码
        username = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        self.root.destroy()
        lg = login()
class login:

    def __init__(self):


        self.root = tk.Tk()
        self.root.title = "用户登陆"
        self.root.geometry('450x300')
        tk.Label(self.root, text='用户名:').place(x=120, y=100)
        tk.Label(self.root, text='密码:').place(x=120, y=150)
        # 用户名输入框
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self.root, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=180, y=100)
        # 密码输入框
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.root, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=180, y=150)

        self.bt_login = tk.Button(self.root, text='注册', command=self.register)
        self.bt_login.place(x=130, y=180)

        self.bt_login = tk.Button(self.root, text='登录', command=self.login)
        self.bt_login.place(x=280, y=180)
        self.root.mainloop()

    def login(self):
        #
        #
        #         global username
        #         # 输入框获取用户名密码
        username = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        self.root.destroy()
        windows = win(username)
        t = threading.Thread(target=init, args={windows, })
        t.start()
        windows.place()
    def register(self):

        self.root.destroy()
        rg = register()



class win:

    def __init__(self,title):

        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_sys)
        self.root.title(title)
        self.root.geometry('500x300')
        self.show = tk.Text(self.root,width=70,height=18)
        self.input = tk.Entry(self.root, width=60)
        self.send_bt = tk.Button(self.root,text="发送信息",command=self.send)

    def send(self):

        msg = self.input.get()
        data = {
            "type":"msg",
            "data":{"from_user":username,"msg":msg}
        }
        send_message(data)
        self.show_msg(data["data"]["from_user"],"\n" + data["data"]["msg"])

    def place(self):

        self.show.pack()
        self.input.pack(side='left')
        self.send_bt.pack(side='right')
        self.root.mainloop()

    def show_msg(self,from_user,msg):

        str_time = time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
        self.show.insert(tk.END, from_user + "  " + str_time)
        self.show.insert(tk.END, msg + "\n")
        self.input.delete(0, tk.END)

    def recv(self,from_user,msg):

        self.show_msg(from_user,msg)

    def someone_leave(self,from_user):

        self.show_msg(from_user," 离开了聊天室...\n\n")

    def new_conn(self,from_user):

        self.show_msg(from_user," 加入了聊天室...\n\n")

    def exit_sys(self):

        data_dict = {
            "type": "exit",
            "data": {"from_user": username}
        }
        send_message(data_dict)
        self.root.destroy()

def send_message(msg):

    msg = json.dumps(msg)
    udp_socket.sendto(msg.encode('GBK'),addr)


def recv_message():

    # 接收数据 并返回接受到的相关数据
    recv_data,client_tuple = udp_socket.recvfrom(1000)
    recv_data = recv_data.decode('GBK')
    recv_data = json.loads(recv_data)
    return {"recv_data":recv_data,"client_tuple":client_tuple}   #数据类型  {"recv_data":{"type":"msg","data":"你好，这里是客户端"},"client_client":('127.0.0.1',1234)}

def show_msg(windows,data): # data:{"from_user":"pzy","msg":"你好呀，这里是新消息"}

    windows.recv(data["from_user"],"\n" + data["msg"])


def someone_leave(windows,data): # data: {"from_user":"pzy"}
    windows.someone_leave(data["from_user"])

def new_conn(windows,data):


    windows.new_conn(data["from_user"])# data: {"from_user":"pzy"}

func = {
    "msg":show_msg,
    "exit":someone_leave,
    "new_conn":new_conn
}
def init(windows):

    data = {"type": "connect", "data": {"username": username}}
    send_message(data)
    while True:
        data_dict = recv_message()
        func[data_dict["recv_data"]["type"]](windows, data_dict["recv_data"]["data"])
    udp_socket.close()


def main():
    lg = login()


if __name__ == '__main__':
    main()
