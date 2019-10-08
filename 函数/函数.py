# def Sum():
#     print("hello world")
#
# #引用函数
# Sum()
#
# #定义有参数的函数
# def Sum(num1,num2):
#     print(num1+num2)
#
# #调用带参数函数
#
# Sum(1,2)

#定义无限个参数的函数
def Sum(*nums):
    print(*nums)
    result = 0
    for num in nums:
        result +=num
    print(result)

#调用无数个参数函数
# Sum(1,2,3,4,5)

Sum(1,2,3,4,5,6,7)

