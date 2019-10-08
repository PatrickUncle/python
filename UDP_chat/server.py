import socket
import json



# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 确定服务器ip地址与端口号
ip_port = ('127.0.0.1',8080)

# 用来存储每个客户端的列表
client_list = []



def send_message(msg,client_tuple):


    msg = json.dumps(msg)

    udp_socket.sendto(msg.encode('GBK'), client_tuple)


def recv_message():
    # 接收数据 并返回接受到的相关数据

    recv_data,client_tuple = udp_socket.recvfrom(1000)
    recv_data = recv_data.decode('GBK')
    recv_data = json.loads(recv_data)
    return {"recv_data":recv_data,"client_tuple":client_tuple}   #数据类型  {"recv_data":{"type":"msg","data":"你好，这里是客户端"},"client_client":('127.0.0.1',1234)}

def new_conn(data,client_tuple): # msg  "用户名"


    us = {
        "username":data["username"],
        "client_tuple":client_tuple
    }

    client_list.append(us)
    for client in client_list:

        if client["client_tuple"] != client_tuple:
            data_dict = {
                "type":"new_conn",
                "data":{"from_user":data["username"]}
            }
            send_message(data_dict,client["client_tuple"])
def transimit(data,client_tuple):


    for client in client_list:

        if client["client_tuple"] != client_tuple:

            data_dict = {
                "type": "msg",
                "data": {"from_user": data["from_user"],"msg":data["msg"]}
            }
            send_message(data_dict, client["client_tuple"])

def someone_leave(data,client_tuple):


    for client in client_list:  # 先将它remove  再进行遍历，否则会出现遍历结果出错，可能列表遍历底层还是按照下标索引进行的！
        if client["client_tuple"] == client_tuple:
            client_list.remove(client)


    for client in client_list:
        if client["client_tuple"] != client_tuple:
            data_dict = {
                "type":"exit",
                "data":{"from_user":data["from_user"]}
            }
            send_message(data_dict,client["client_tuple"])



func = {
    "connect":new_conn,
    "msg":transimit,
    "exit":someone_leave
}
def init():


    udp_socket.bind(ip_port)
def main():


    init()
    while True:
        data_dict = recv_message()
        func[data_dict["recv_data"]["type"]](data_dict["recv_data"]["data"],data_dict["client_tuple"])

    # 关闭
    udp_socket.close()


if __name__ == '__main__':


    main()