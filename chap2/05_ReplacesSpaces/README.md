# 面试题5：替换空格

**【题目】：**  请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

例如：输入“We are happy.”,则输出““We%20are%20happy.”





LeetCode:[替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)





【解题思路】

解法一：先将字符串的各个元素都取出，放到数组中。对数组元素进行修改，再将修改后的元素拼接起来。

```python
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
```

**拓展题目**

**【题目】：**  给你两个有序整数数组 *nums1* 和 *nums2*，请你将 *nums2* 合并到 *nums1* 中*，*使 *nums1* 成为一个有序数组。

说明：

- 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
- 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

**示例：**

```Python
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]
```

LeetCode:[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)



【解题思路】

1. 采用类外排法进行合并数组，排序顺序是从大排序到小；
2.  若num1的初始化空间大于m+n，即此时index>0， 将已经排序好的num1数组数值元素向前移动index个位置，剩余的位置全部置0

```Python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length=len(nums1)   # num1数组长度
        # 采用类外排法进行合并数组，排序顺序是从大排序到小
        index1=m-1          # 两个数组的移动下标
        index2=n-1
        index=length-1      # 合并数组的移动下标

        while index1>=0 and index2>=0:
            if nums1[index1]>=nums2[index2]:
                nums1[index]=nums1[index1]
                index1 -=1
            else:
                nums1[index]=nums2[index2]
                index2 -=1
            index -=1
        # 至少一个数组被遍历结束
        if index1>=0:
            while index1>=0:
                nums1[index]=nums1[index1]
                index1 -=1
                index -=1
        elif index2>=0:
            while index2>=0:
                nums1[index]=nums2[index2]
                index2 -=1
                index -=1
        
        # 若num1的初始化空间大于m+n，即此时index>0
        # 将已经排序好的num1数组数值元素向前移动index个位置，剩余的位置全部置0
        if m+n<length:
            # num1数组初始化时多出的空间，即
            # num1数组需要置0的区间的长度
            gap=length-m-n   

            for i in range(m+n):
                nums1[i]=nums1[i+gap]
            for j in range(m+n,length):
                nums1[j]=0
```

