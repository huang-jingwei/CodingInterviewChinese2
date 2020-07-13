# 面试题42：连续子数组的最大和

**题目描述：** 输入一个整形数组，数组里有正数也有负数。数组中的一个或者连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为：O(N)

例如：输入的数组为{1,-2,3,10,-4,7,2,-5},那么最大子数组为{3,10,-4,7,2},因此输出为该子数组的和为18.



LeetCode:[连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)



**思路一：暴力解法，穷举所有可能的子数组**

基本思想：可以将给定数组的的所有子数组列出来，然后找到子数组和做大的情况，具体来说就是： 对数组内每一个数A[i]进行遍历，然后遍历以它们为起点的子数组，比较各个子数组的大小，找到最大连续子数组；

算法复杂度为：O(n^2)。

```python
#函数功能：采用穷举的方法找到连续子数组的最大和
#算法复杂度：O(N^2)
def GetLeastNumbers_right(array):
    if array==None or len(array)<=0:   #对数组进行判空操作
        return None
    elif len(array)==1:               #数组只有一个元素时，直接返回该元素数值
        return array[0]
    maxSubArraySum=array[0]           #连续子数组最大和
    for i in range(len(array)):
        count=0                       #记录从下标i所有可能的连续子数组的和
        for j in range(i,len(array)):
            count=count+array[j]
            if count>=maxSubArraySum:
                maxSubArraySum=count
    return maxSubArraySum
```



**思路二：**

用total记录累计值，maxSum记录和最大

基于思想：对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对整体和是有贡献的。如果前几项累计值负数，则认为有害于总和，total记录当前值。

此时 若和大于maxSum 则用maxSum记录下来。最后返回maxSum。

算法时间复杂度O（n）



```python
#函数功能：找到数组的连续子数组最大和

# 基于思想：对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对整体和是有贡献的。
# 如果前几项累计值负数，则认为有害于总和，total记录当前值。
# 此时 若和大于maxSum 则用maxSum记录下来。最后返回maxSum。
#算法时间复杂度O（n）
def GetLeastNumbers(array):
    if array==None or len(array)<=0: #对数组进行判空操作
        return None
    elif len(array)==1:                  #数组只有一个元素时，直接返回该元素数值
        return array[0]
    total =array[0]                      #初始化当前子数组总和数值
    maxSum=array[0]                      #初始化连续子数组最大和
    for index in range(1,len(array)):    #遍历数组
        if total>=0:
            total=total+array[index]
        else:
            total=array[index]
        if total>=maxSum:
            maxSum=total
    return maxSum
```







