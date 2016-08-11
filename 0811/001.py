'''
Created on 2016年8月11日

@author: mazkun
'''
import random
import string


def random_num(number = 200, length = 8):
    char_set = string.ascii_letters + string.digits + "@#$%^&*"
    result  = ""
    for i in range(0, number):
        temp = ""
        while(temp == ""):
            for j in range(0, length):
                temp = temp + char_set[random.randint(0, 35)]
            if(result.find(temp) == -1):
                result = result + "%d "%(i + 1) + temp
            else:
                temp = ""
        result = result + "\n"
    print(result)
    return result
def file_write():
    fp = open("result.txt", "w")
    fp.writelines(random_num())
    fp.close()

if __name__ == "__main__":
    file_write()