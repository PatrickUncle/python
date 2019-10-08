import time
import datetime

# t = time.time()
# print(t)
# print(type(t))
# print("-------------------------------------")
# str0 = time.ctime(t)
# print(str0)
# print(type(str0))
# print("-------------------------------------")
# t_puple = time.strptime(str0)
# print(t_puple)
#
#
# result = time.strftime("%Y-%m-%d %H:%M:%S",t_puple)
# print(result)

now = time.time()
print(now)
print(datetime.date)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(type(time.localtime()))

shijian = "2018-04-05"
t = time.strptime(shijian,"%Y-%m-%d")
print(t)
print(datetime.datetime.now())
print(type(datetime.datetime.now()))