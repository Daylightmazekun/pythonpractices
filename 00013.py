'''
Created on 2016年7月31日

@author: Administrator
'''
import re
from urllib import request
import urllib


url = "http://tieba.baidu.com/p/2166231880"#网站地址

urlhd = urllib.request.Request( url, headers = {#报头
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })

page = urllib.request.urlopen(urlhd)

try:
    data = page.read().decode('utf-8')
except:
    exit(0)


imgre = re.compile(r'src=\"(.*?)\"')
result = imgre.findall(data)
picnum = 0
for x in result:
    if '.jpg' not in x:
        continue
    img = urllib.request.urlopen(x, timeout = 3).read()
    try:
        f = open(str(picnum)+'.jpg','wb')
        f.write(img)
        picnum+=1
        f.close()
        
    except:
        print("无法将图片%s写入%s"% (x, str(picnum) + 'jpg'))

        
    
    
