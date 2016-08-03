'''
Created on 2016年7月31日

@author: Administrator
'''
import os
import urllib

from bokeh.io import save
from bs4 import BeautifulSoup


def get_img_src_list(url, img_class):
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content)#读取网页html 代码 讲代码元素分离
    #print soup
    src_list = []
    for img in soup.find_all('img', img_class):#找到页面中所有的img标签 以及标签类为img_class的部分
        src_list.append(img['src'])
    
    return src_list
def download_img(src, download_path):
    print("Begin download image: %s...." % src)
    file_name = src.split("/")[-1]
    dist = os.path.join(download_path, file_name)
    urllib.request.urlretrieve(src, dist, None)
    print("Download image %s Done" %src)
    

if __name__ == "__main__":
    src_list = get_img_src_list('http://tieba.baidu.com/p/2166231880', 'BDE_Image')
    if src_list:
        save_path = os.path.abspath("./download")
        if not os.path.exists(save_path):          
            os.mkdir(save_path)
        print("start download %d images...."% len(src_list))
        
        for src in src_list:
            download_img(src, save_path)

        print("download %d imges done." %len(src_list))
        
        
    else:
        print("No Imges found!!!")
        
        
        