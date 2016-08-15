'''
Created on 2016年8月9日

@author: mazkun
'''
from PIL import Image, ImageDraw, ImageFont


img = Image.open('weChat_avatar.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("verdana.ttf", 100)
draw.text((img.size[0]-100, 30), "3",(255, 0, 0), font)
img.save("result.jpg")