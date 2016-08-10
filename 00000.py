'''
Created on 2016年8月10日

@author: mazekun
'''
from PIL import Image, ImageDraw, ImageFont


def draw_number(path = './', num = 4): 
    im = Image.open(path)
    size = im.size
    fontsize = size[0]/4
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("verdana.ttf", fontsize)
    draw.text((3*fontsize,0), str(num), (255, 0, 0), font)
    im.save("success.png", "PNG")
    


if __name__ == "__main__":
    draw_number()