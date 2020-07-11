import  numpy as np
import random

#函数功能：找出数组中重复的数字
#思路二：基于哈希表
#算法复杂度:O(N)
def duplicate(array):
    if array==None or len(array)<=0:    #判断数组是否为空数组
        return None
    hashMap={}                          #用来记录数组中元素是否是重复元素
    for index in range(len(array)):
        if array[index] not in hashMap: #若字典中没存在该元素，则将该元素添加到字典中
            hashMap[array[index]]=1
        else:                           #若字典中已经存在该元素，则直接返回
            return array[index]

#对照组实验
#思路一：先对数组进行排序在进行搜索
def duplicate_right(array):
    if array==None or len(array)<=0:    #判断数组是否为空数组
        return None
    sortArray=sorted(array)
    for index in range(len(sortArray)-1):
        if sortArray[index]==sortArray[index+1]:
            return sortArray[index]
    return False
