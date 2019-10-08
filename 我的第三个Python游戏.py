print("------欢迎来到彭祖宇的第一个Python游戏！------\n")
i = 0;
delay = 0
count = 0
while 1:
    if count == 50:
        print("正在建造第"+ str(i) + "个敌机！\n")
        i=i+1
        count = 0
    count = count + 1
    print("刷新游戏界面中")
    while delay <1000000:
        delay=delay+1
    delay = 0
    
    
    
