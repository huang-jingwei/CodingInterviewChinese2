# 面试题53：在排序数组中查找数字



【题目】 统计一个数字在排序数组中出现的次数。

例如：统计一个数字在排序数组中出现的次数。例如，输入排序数组{1、2、3、3、3、3、4、5}和数字3，由于3在这个数组中出现了4次，因此输出4



**思路一：暴力解法**

最简单直接的方法就是每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对。

算法时间复杂度：O(N)

LeetCode:[在排序数组中查找数字](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==None or len(nums)<1:
            return 0
        count=0
        for index in range(len(nums)):
            if nums[index]==target:
                count=count+1
        return count
```



**思路二：二分查找**

LeetCode:[在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)



```python
def
```



