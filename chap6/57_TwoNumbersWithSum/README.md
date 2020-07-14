# 面试题57-1：和为s的两个数字

【题目一】输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



LeetCode:[和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)



**思路一：暴力解法**

最简单直接的方法就是直接遍历数组。

算法时间复杂度：O(N^2)

```Python
# 函数功能： 找出数组中和为s的两个数字
# 基本思路：最简单直接的方法就是直接遍历数组
# 算法时间复杂度：O(N^2)
def TwoNumbersWithSum_right(array,s):
    if array== None or len(array)==0:     # 若输入数组为空，直接输出0
        return False
    for index in range(len(array)):       # 遍历数组
        for anotherIndex in range(len(array)):
            if array[index]+array[anotherIndex]==s and index!=anotherIndex:
                return [array[index],array[anotherIndex]]
```



**思路二：哈希表**

算法时间复杂度：O(N)

```python
# 函数功能： 找出数组中和为s的两个数字
# 基本思路：等差数列的求和公式sum=(a1+an)*n/2
# 算法时间复杂度：O(N)
def TwoNumbersWithSum_right(array,s):
    if array== None or len(array)==0:     # 若输入数组为空，直接输出0
        return False
    data={}                               # 初始化一个字典，模拟哈希表，用来存放数组的数值
    for index in range(len(array)):       # 在哈希表中，key：数组中元素，value：该元素在数组中第一次出现时对应的下标
        if array[index] not in data:
            data[array[index]]=index
    for key,value in data.items():        # 遍历哈希表
        if s-key in data:
            return [key,s-key]
```



这道题目也可以采用二分查找的方法来进行求解。算法时间复杂度：O(N log N)，因为算法时间复杂度没有比思路二的哈希表好。下面就只讲基本思路：

1、先确定第一个数array[index]，记录下该元素的数值value和对应的下标index

2、采用二分查找的方法判断s-array[index]是否在数组array中，这点需要满足两个条件：

①s-array[index]在数组array中

②数值s-array[index]在数组array中对应的数值的下标必须要和index不一样才行



# 面试题57-2： 和为s的连续正数序列

【题目二】输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



例如：

```python
输入：target = 9
输出：[[2,3,4],[4,5]]
```

```python
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

LeetCode:[和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)