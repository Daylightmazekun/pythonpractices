'''
Created on 2016年7月24日

@author: Administrator
'''
def check():
    with open('filtered_words.txt', 'r', encoding = 'utf-8')as f:
        data = f.read()
    filt = data.split('\n')
    
    while True:
        text = input("please input your check words:")
        
        for x in filt:
            if text.find(x) != -1:
                text = text.replace(x, '*'*len(x)) 
            print (text)   
    


if __name__ == '__main__':
    check()