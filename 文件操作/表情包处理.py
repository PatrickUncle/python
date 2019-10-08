import os

face_list = os.listdir(r"E:\images")
for face in face_list:
    if "狗日" in face:
        print(face)
