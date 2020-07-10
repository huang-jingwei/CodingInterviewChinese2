import  numpy as np
import random


#对数器模块


#交换列表两个不同索引下标的数值
def swap(array,index1,index2):
    item=array[index1]
    array[index1]=array[index2]
    array[index2]=item
    return array


#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array
