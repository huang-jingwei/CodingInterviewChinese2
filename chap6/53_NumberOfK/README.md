# 面试题53：在排序数组中查找数字



【题目一】 统计一个数字在排序数组中出现的次数。

例如：统计一个数字在排序数组中出现的次数。例如，输入排序数组{1、2、3、3、3、3、4、5}和数字3，由于3在这个数组中出现了4次，因此输出4



LeetCode:[在排序数组中查找数字](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)



**思路一：暴力解法**

最简单直接的方法就是每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对。

算法时间复杂度：O(N)

```Python
# 函数功能： 统计一个数字在排序数组中出现的次数
# 基本思路：遍历数组array来进行统计数字k出现的次数
# 算法时间复杂度：O(N)
def NumberOfK_right(array,k):
    if array== None or len(array)==0:       # 若输入数组为空，直接输出0
        return 0
    count = 0                               # 初始化计数器，用来记录数字k在数组array中出现的次数
    for index in range(len(array)):         # 遍历数组
        if array[index]==k:
            count=count+1
    return count
```



**思路二：二分查找**







