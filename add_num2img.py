'''
Created on 2016年8月10日

@author: mazekun
'''
import sys

from PIL import Image, ImageDraw, ImageFont


def add_num_to_img(file_path):
    im = Image.open(file_path)
    im_draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("verdana.ttf", int(im.size[0]/5))
    im_draw.text((int(im.size[0] - im.size[0]/10), 5), "4", (256, 0, 0), font = font)
    #位置 要写什么 颜色 字体
    del im_draw
    im.save('./result.png')



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("need at least 1 parameter , try to execute 'py'")
    else:
        for infile in sys.argv[1:]:
            try:
                add_num_to_img(infile)
                print("good game")
            except IOError:
                print("GG")
                pass    
                   