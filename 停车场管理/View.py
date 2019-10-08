import time
park_list = []
leave_list = []

def stop():
    drive_id = input("请输入车牌号：")
    data = {
        "time":time.time(),
        "drive_id":drive_id
    }
    park_list.append(data)
def leave():
    drive_id = input("请输入车牌号:")
    for park in park_list:
        if park["drive_id"] == drive_id:
            park_list.remove(park)
            park["time"] = time.time()
            leave_list.append(park)
def show_park():
    print("车牌号    到达时间")
    for park in park_list:
        print(park["drive_id"],park["time"])
def show_leave():
    print("车牌号    离开时间")
    for park in leave_list:
        print(park["drive_id"], park["time"])
def menu():
    print("请选择服务项目：")
    print("1.停车")
    print("2.离开")

def menu2(t):
    print(t)
    print("请选择操作类型：")
    print("1.输入")
    print("2.输出")

def init():
    print("系统正初始化中，请稍后。。。")

def main():
    init()
    while True:
        menu()
        choice = int(input())
        if choice == 1:
            menu2("停车")
            secound = int(input())
            if secound == 1:
                stop()
                show_park()
            elif secound == 2:
                show_park()
            else:
                continue
        elif choice == 2:
            menu2("离开")
            secound = int(input())
            if secound == 1:
                leave()
                show_leave()
            elif secound == 2:
                show_leave()
            else:
                continue
        else:
            break
if __name__ == '__main__':
    main()