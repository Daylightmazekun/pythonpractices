'''
Created on 2016年8月11日

@author: mazekun
'''
import random
import string


def randomSetquence(r, l):
    
    
    for i in range(r):
        s = string.ascii_letters + string.digits + '@#$%^&*'
        random_seq = []
        sl = list(s)
        
        for i in range(10):
            random.shuffle(sl)
            random_seq.append(''.join(sl[:1]))
            
        print(random_seq)
    return random_seq
    


if __name__ == "__main__":
    result = randomSetquence(200, 8)

    
            