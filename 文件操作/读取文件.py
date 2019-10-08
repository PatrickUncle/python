f = open(file=r'text.txt',mode='r',encoding='utf-8')
# data = f.read()
# print(data)
for data in f:
    print(data)
f.close()