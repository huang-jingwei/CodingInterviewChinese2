import  numpy as np
import random

#函数功能：把字符串 s 中的每个空格替换成"%20"
#解法一：利用Python数据结构的特性
#基本思路：先将字符串的各个元素都取出，放到数组中。对数组元素进行修改，再将修改后的元素拼接起来。
def ReplacesSpaces_right(s):
    array = [s[i] for i in range(len(s))]
    for i in range(len(array)):
        if array[i] == " ":
            array[i] = '%20'
    string = ""
    for i in range(len(array)):
        string = string + array[i]
    return string

if __name__=="__main__":
    s="We are happy."
    print(s)
    print(ReplacesSpaces_right(s))


