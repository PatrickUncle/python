# _*_ utf-8 _*_
import  os
BASE_PATH = r"F:\书籍封面图片"

def deal(file_name):
    file_path = os.path.join(BASE_PATH,file_name)
    new_name = os.path.join(BASE_PATH,file_name.split(".")[0] + ".jpg")
    os.rename(file_path,new_name)


if __name__ == '__main__':
    cover_list = os.listdir(BASE_PATH)
    for cover in cover_list:
        if cover.split(".")[1] == "jpg_400x400":
            deal(cover)
            print(cover)
