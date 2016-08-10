'''
Created on 2016年8月10日

@author: mazekun
'''
from PIL import ImageFont, Image, ImageDraw


def save_image():
    myfont = ImageFont.truetype("verdana.ttf", 35)
    im = Image.open('touxiang.png')
    draw = ImageDraw.Draw(im)
    x, y = im.size
    draw.text((x-x/5, y/8), "8", fill=(255, 0, 0), font = myfont)
    im.save("result.png", "PNG")
    
if __name__ == '__main__':
    save_image()