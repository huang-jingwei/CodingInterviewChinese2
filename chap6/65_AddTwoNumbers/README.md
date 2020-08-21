# 面试题65：不用加减乘除做加法

【题目】写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

例子

```python
输入: a = 1, b = 1
输出: 2
```

LeetCode:[不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)



**思路一：暴力解法**

```Python
class Solution:
    def add(self, a: int, b: int) -> int:
        return a+b
```





**思路二**

算法时间复杂度：O(N)

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        listLength=len(a)
        if listLength==0:
            return []
        elif listLength==1:
            return a
   
        #left[index]:代表A[0]*A[1]*...*A[index-1]
        left=[1]*listLength  
        for index in range(1,listLength):
            left[index]=left[index-1]*a[index-1]
        
        #right[index]:代表A[index+1]*A[index+2]*...*A[listLength-1]
        right=[1]*listLength  
        for index in range(listLength-2,-1,-1):
            right[index]=right[index+1]*a[index+1]
        
        answer=[1]*listLength  
        for index in range(listLength):
            answer[index]=left[index]*right[index]
        return answer         
```

