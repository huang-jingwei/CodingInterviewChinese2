# 面试题62：圆圈中最后剩下的数字

【题目】0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。



例子

```python
输入: n = 5, m = 3
输出: 3
    
输入: n = 10, m = 17
输出: 2
```

LeetCode:[圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)



**解题过程**



```Python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return -1

        number = list(range(n))  # 目标列表
        begin = 0                # 下标与index=begin之间的距离为m的数即为所要删除的数值
        while len(number) > 1:
            delIndex = (begin + m - 1) % len(number)
            del number[delIndex]
            begin = delIndex
        return number[0]
```



