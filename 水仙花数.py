#获取该数
for num in range(1,1000000000):
#将该数的所有位数都取出来
    str1 = str(num)
    result = 0
    for temp in str1:
        temp = int(temp)
        center = 1
        for i in range(0,len(str1)):
            center *=temp
        result += center
    #进行判断，若是的，则输出，否则不输出
    if result == num:
        print(num)
