import os
path = r"C:\Users\ASUSPC\Desktop\python.txt"
if os.path.exists(path):
    os.remove(path)
else:
    print("can't find the file:%s"%path)