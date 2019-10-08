from PIL import Image
f_path = r"C:\Users\ASUSPC\Desktop\20180122205408244.gif"

WIDTH = 90
HEIGHT = 45
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):  # alpha透明度
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符
    # 通过灰度来区分色块
im = Image.open(f_path)
print(im.mode)
i = 0
while True:
    i += 1
    im.seek(i)
    print(im)
    # txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(type(im.getpixel((j, i))))
    #         # txt += get_char(*im.getpixel((j, i)))
    #     txt += '\n'
    # print(txt)


