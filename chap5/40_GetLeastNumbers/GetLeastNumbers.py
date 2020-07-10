import random

#函数功能：找出数组中最小的k个数
#解题思路：采用荷兰国旗问题的partition过程
#算法复杂度:O(N)

def GetLeastNumbers(array,k):
    if array==None or len(array)==0:   #对数组进行判空操作
        return None
    if k<=0 or k>=len(array):          #判断数值k的合理性
        return None
    if k==len(array)-1:                #当k等于数组长度时，直接返回原数组
        return array
    left=0                                        #数组array操作区间左边界下标
    right=len(array)-1                            #数组array操作区间右边界下标
    indexRange=partition(array, left, right)      #对整个数组array进行partition过程
    while k<indexRange[0] or k>indexRange[1]:     #所得区间不能包含中位数下标时，调用递归函数
        if k < indexRange[0]:                     #中位数下标比所得区间左边界下标还小时，对区间数组左侧再进行partition过程
            right = indexRange[0]
            indexRange = partition(array, left, right)
        elif k>indexRange[1]:
            left=indexRange[1]
            indexRange = partition(array, left, right)
    return array[:k]


#荷兰国旗问题
#函数功能：任选数组一个值num，要求把数组中小于num的元素放到数组的左边，大于num的元素放到数组的右边，等于num的元素放到数组的中间
# 最终返回一个整数数组，其中只有两个值，分别是等于num的数组部分的左右两个下标值。
#参数说明：array：给定的数组，left：数组操作区间的左边界下标，right：数组操作区间的的右边界下标

def partition(array,left,right):
    num=array[random.randint(left,right)]  #在数组操作区域区间内任选一个数
    index=left                             #移动下标
    less=left-1                            #array数组中，下标≤less的区域存放小于num的数
    more=right+1                           #array数组中，下标≥more的区域存放大于num的数
    while index<more:
        if array[index]==num:
            index=index+1
        elif array[index]<num:
            less=less+1
            array[index],array[less]=array[less],array[index]
            index=index+1
        elif array[index]>num:
            more=more-1
            array[index],array[more]=array[more],array[index]
    indexRange=[less+1,more-1]             #等于num的数组部分的左右两个下标值
    return indexRange


######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

if __name__=="__main__":


    # 采用对数器方法进行对所写代码进行验证,找出数组中最小的k个数
    # 这里验证的时为了验证结果的统一，对所得的列表调用库函数排序
    errorCount = 0                            # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                          # 随机数列表的长度
        k=50                                  # 找出数组中最小的k个数
        array = randomList(length)            # 生成随机数列表
        sortArray = sorted(array)             # 采用库函数对原随机数列表进行升序排序，sorted函数不会改动原数组
        right = sortArray[:k]                 # 找出数组中最小的k个数
        test = GetLeastNumbers(array,k)       # 自己编写的算法,找出数组中最小的k个数
        test=sorted(test)
        if right == test:
            print ("第%d次测试：测试准确" % (i))
        else:
            print ("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print ("测试过程中算法求解错误的次数%d" % (errorCount))