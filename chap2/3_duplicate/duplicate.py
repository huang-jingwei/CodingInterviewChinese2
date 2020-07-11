import  numpy as np
import random

#函数功能：找出数组中出现次数超过一半的数字
#解题思路：将该问题转化成求解数组中位数的问题
#算法复杂度:O(N)

def duplicate(array):
    if array==None or len(array)==0:              #判断数组是否为空数组
        return None
    left=0                                        #数组array操作区间左边界下标
    right=len(array)-1                            #数组array操作区间右边界下标
    mid=(right+left)//2                           #数组array中位数的下标
    indexRange=partition(array, left, right)      #对整个数组array进行partition过程
    while mid<indexRange[0] or mid>indexRange[1]: #所得区间不能包含中位数下标时，调用递归函数
        if mid<indexRange[0]:                     #中位数下标比所得区间左边界下标还小时，对区间数组左侧再进行partition过程
            right=indexRange[0]
            indexRange = partition(array, left, right)
        elif mid > indexRange[1]:                 #中位数下标比所得区间右边界下标还大时，对区间数组右侧再进行partition过程
            left = indexRange[1]
            indexRange = partition(array, left, right)
    return array[mid]



######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

#对照组实验
def duplicate_right(array):
    if array==None or len(array)<=0:    #判断数组是否为空数组
        return None
    hashMap={}                          #用来记录数组中元素是否是重复元素
    for index in range(len(array)):
        if array[index] not in hashMap: #若字典中没存在该元素，则将该元素添加到字典中
            hashMap[array[index]]=1
        else:                           #若字典中已经存在该元素，则直接返回
            return array[index]

if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证，找出数组中重复的数值
    # 这里验证的时是替代问题，即数组中位数求解是否准确
    errorCount=0                        #记录测试过程中算法求解错误的次数
    for i in  range(10000):
        length=500                      #随机数列表的长度
        array=randomList(length,low=0,high=length) #生成随机数列表
        right=duplicate_right(array)               #对数器函数，用来做对照组实验
        test=duplicate(array)                      #自己编写的算法
        if right==test:
            print ("第%d次测试：测试准确"%(i))
        else:
            print ("第%d次测试：测试错误"%(i))
            errorCount=errorCount+1
    print ("测试过程中算法求解错误的次数%d"%(errorCount))


