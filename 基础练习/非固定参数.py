
#元组形式
def send_msg(msg,*users):
    for user in users:
        print(msg,":",user)


send_msg("发送消息给","pzy","psh") #传进来的参数，是元组形式，然后就可以进行遍历

send_msg("发送消息给",*["aaa","ggg"]) #将一个列表传进去，然后变成元组。

def send_msg1(msg,*users,**kwargs):
    print(msg,users,kwargs)

send_msg1("fsss","a","b","c",addr="山东",ppp="ooo") #**是第二种非固定参数，如果使用函数中没有的固定参数来指定实参，那么将会传给 kwargs组成字典