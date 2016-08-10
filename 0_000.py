'''
Created on 2016年8月10日

@author: mazekun
'''
from PIL import Image, ImageFont, ImageDraw


def add_number(num):
    im = Image.open("icon.png")
    text = Image.new('RGBA', im.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype("verdana.ttf", 40)
    d = ImageDraw.Draw(text)
    d.text((im.size[0]-50, 5), str(num), font = fnt, fill = (255, 0, 0, 255))
    out = Image.alpha_composite(im, text)
    out.show()
    out.save("icon_"+str(num)+".png")
if __name__ == "__main__":
    add_number(42)