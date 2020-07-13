# 面试题40：最小的k个数

**题目：**  输入n个整数，找出其中最小的k个数。



**例如：** 输入4、5、1、6、2、7、3、8。则最小的4个数字是1、2、3、4。



LeetCode：[最小的K个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)



**思路一：**  先将输入n个整数进行排序，排序排序之后最前面的k个数就是最小的k个数

快速排序算法的时间复杂度：O(N)

**思路二：**  基于partition函数

可以基于partition函数来解决这个问题。如果基于数组的第k个数字来调整，则使得比第k个数字小的所有数组都位于数组的左边，比第k个数字大的所有数组都位于数组的右边。这样调整后，位于数组中左边的k个数字就是最小的k个数字（注意：这k个数字不一定是排序的）



```python
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
```

