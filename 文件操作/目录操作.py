import os

Base_path = r"G:\beauty_test"

path_list = os.listdir(Base_path)
print(path_list)
id_list = []
for path in path_list:
    id = os.listdir(os.path.join(Base_path,path))
    print(id)
    id_list.extend(id)
print(id_list)
id_list.sort()
print(id_list)
id_list.reverse()
print(id_list)

print(os.getcwd())
print(os.path.abspath(os.path.join(os.getcwd(),"../")))
