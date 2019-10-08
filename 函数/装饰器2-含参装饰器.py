
#需求：
#    当需要对结果进行筛选时，便需要对搜索结果加以控制，需要传参
#

loading_confirm = False

def loading(func):
    def inner(*arg):

        global loading_confirm
        if loading_confirm == False:
            print("输入账号密码")
            loading_confirm = True

        if loading_confirm:
            func(*arg)
    return inner



def home():
    print("首页")

def action(actor):
    print("动作片")

def comedy():
    print("喜剧片")

def dracula():
    print("恐怖片")


action = loading(action)

action("周星驰")