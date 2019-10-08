from PIL import Image

def resize_by_size(width,height):
    im =Image.open(r"C:\Users\ASUSPC\Desktop\python\images\sushiplate.jpg")
    out = im.resize((width,height),Image.ANTIALIAS)
    out.save(r"C:\Users\ASUSPC\Desktop\python\images\sushiplate1.jpg")
resize_by_size(100,100)