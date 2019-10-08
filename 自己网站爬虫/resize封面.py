# _*_ utf-8 _*_
from PIL import Image
import os
BASE_PATH = r"C:\Users\ASUSPC\Desktop\书的封面"
NEW_PATH = r"C:\Users\ASUSPC\Desktop\书的封面"

HEIGHT = 380
WIDTH = 306

def resize(url):
    filename = url.split("\\")[-1]
    im = Image.open(url)
    new_img = im.resize((WIDTH,HEIGHT),Image.ANTIALIAS)
    new_img.save(os.path.join(NEW_PATH,filename))

if __name__ == '__main__':
    cover_list = os.listdir(BASE_PATH)
    for cover in cover_list:
        resize(os.path.join(BASE_PATH,cover))


