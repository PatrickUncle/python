import socket,select

host = socket.gethostname()
port = 5963
server_addr = (host,port)

# waitable的read list, 表示异步通信中可读socket对象的列表
inputs = []
# 连接进入server的client的名称
fd_name = {}

# 创建并初始化server socket
def serverInit():
    ss = socket.socket()  # 创建server socket
    ss.bind(server_addr)  # 绑定到server addr
    ss.listen(10)          # 监听端口号, 设置最大监听数10
    return ss             # 返回初始化后的server socket

# 创建一个新的socket连接
def newConnection(ss):
    client_conn,client_addr = ss.accept()  # 响应一个client的连接请求, 建立一个连接,可以用来传输数据
    try:
        # 向client端发送欢迎信息
        client_conn.send(bytes("welcome to chatroom,pls set up your nick name!",encoding="utf8"))
        client_name = client_conn.recv(1024) #接收client发来的昵称,最大接收字符为1024
        print(client_name)
        inputs.append(client_conn)
        fd_name[client_conn] = client_name  # 将连接/连接名 加入键值对
        client_conn.send("current members in chatroom are: %s" % fd_name.values())
        # 向所有连接发送新成员加入信息
        for other in fd_name.keys():
            if other != client_conn and other != ss:
                other.send(fd_name[client_conn]+" joined the chatroom!")
    except Exception as e:
        print(e,"1")

def closeConnection():
    pass

def run():
    ss = serverInit()
    inputs.append(ss)
    print("server is running...")
    while True:
        # rlist,wlist,elist = select.select(inputs, [], inputs,100)   # 如果只是服务器开启,100s之内没有client连接,则也会超时关闭
        rlist,wlist,elist = select.select(inputs, [], [])
        # 当没有可读fd时, 表示server错误,退出服务器
        if not rlist:
            print("timeout...")
            ss.close()  # 关闭 server socket
            break
        for r in rlist:
            if r is ss:  # server socket, 表示有新的client连接请求
                newConnection(ss)
            else:          # 表示一个client连接上有数据到达服务器
                disconnect = False
                try:
                    data = r.recv(1024)  #接收data
                    data = fd_name[r] + " : "+ data  # 确定客户端昵称
                except socket.error:
                    data = fd_name[r] + " leaved the room"
                    disconnect = True
                else:
                    pass
                if disconnect:
                    inputs.remove(r)
                    print(data,"3")
                    for other in inputs:
                        if other != ss and other != r:  #不发生到服务器和已经断开的连接
                            try:
                                other.send(data)
                            except Exception as e:
                                print(e,"4")
                            else:
                                pass
                    # 除名
                    del fd_name[r]
                else:
                    print(data) # 在服务器显示client发送的数据
                    # 向其他成员(连接)发送相同的信息
                    for other in inputs:
                        if other != ss and other != r:
                            try:
                                other.send(data)
                            except Exception as e:
                                print(e)
if __name__ == "__main__":
    run()