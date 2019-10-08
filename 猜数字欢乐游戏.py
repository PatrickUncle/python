import random
#生成随机数
x = random.randint(0,100)

#使用while进行无限循环
while 1:
#获取用户输入
    guess = input("请输入您的猜想数字：")
    guess = int(guess)
    #判断用户输入数字与随机数的大小相等关系
    if guess == x:
        print("you are so smart!")
        break
    else:
        if guess < x:
            print("small,try again")
        else:
            print("big.try again!")