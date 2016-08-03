'''
Created on 2016年7月31日

@author: mazekun
'''
import os
import urllib
from urllib.parse import urlsplit

from bs4 import BeautifulSoup


def catch_tieba_pics(tieba_url):
    content = urllib.request.urlopen(tieba_url)
    bs = BeautifulSoup(content,'lxml')
    for i in bs.find_all('img',{"class":"BDE_Image"}):#找到html页面sou对象的img标签以及标签类为BDE_Image的对象
        download_pic(i['src'])
def download_pic(url):
    image_content = urllib.request.urlopen(url).read()
    #os.path.basename(path) #返回当前路径文件名
    file_name = os.path.basename(urlsplit(url)[2])#返回urlsplit(url)[2]的；路径名
    output = open(file_name,'wb')
    output.write(image_content)
    output.close()

    
    
    
    
    



if __name__ == "__main__":
    tieba_url = "http://tieba.baidu.com/p/2166231880"
    catch_tieba_pics(tieba_url)