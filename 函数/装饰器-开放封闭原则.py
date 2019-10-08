
#需求：
#    在用户点击前要先进行身份验证与登陆
#    在不修改原来已存在的代码的前提下扩展功能

loading_confirm = False

def loading(func):
    def inner():

        global loading_confirm
        if loading_confirm == False:
            print("输入账号密码")
            loading_confirm = True

        if loading_confirm:
            func()
    return inner



def home():
    print("首页")

def action():
    print("动作片")

def comedy():
    print("喜剧片")

def dracula():
    print("恐怖片")


action = loading(action)

# print(action)
# action()