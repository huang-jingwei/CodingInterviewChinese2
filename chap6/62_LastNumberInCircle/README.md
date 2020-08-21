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
    def add(self, a: int, b: int) -> int:
        return a+b
```



