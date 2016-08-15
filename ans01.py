'''
Created on 2016年8月9日

@author: mazekun
'''
original_avatar = 'weChat_avatar.png'
saved_avatar = 'new_avatar.png'
windows_font = 'verdana.ttf'
number = str(4)
color = (255, 0, 0)
def draw_text(text, fill_color, windows_font):
    try:
        im = Image.open(original_avatar)
        x, y = im.size
        print("The size of the Image is:")
        print(im.format, im.size, im.mode)
        
        draw = ImageDraw.Draw(im)
        print(draw)
        font = ImageFont.truetype(windows_font, 35)
        draw.text((x-20, 7), text, fill_color, font)
        im.save(saved_avatar)
        im.show()
    except:
        print("cant do this")
        





from PIL import Image, ImageDraw, ImageFont
if __name__ == "__main__":
    draw_text(number, color, windows_font)