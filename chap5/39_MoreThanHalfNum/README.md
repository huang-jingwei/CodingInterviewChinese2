# 面试题39：数组中出现次数超过一半的数字

**题目：** 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字



**例如：** 输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。



LeetCode：[数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)



**解题思路：基于partition函数**

时间复杂度：O(N)

数组中有一个一个数字出现的次数超过了数组长度的一半。如果将这个数组进行排序，那么排序之后位于数组之间的数字一点是那个出现次数超过数组长度一半的数字。也就是说，这个数字是统计学上的中位数，即长度为n的数组中第n/2大的数字



```python
#函数功能：找出数组中出现次数超过一半的数字
#解题思路：将该问题转化成求解数组中位数的问题
#算法复杂度:O(N)

def MoreThanHalfNum(array):
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
```

