# 面试题17：打印从1到最大的n位数



【题目】输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。



LeetCode:[打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)



说明：

- 用返回一个整数列表来代替打印
- n 为正整数



**思路一：暴力解法**



```Python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result=[]
        value=1
        while value<10**n:
            result.append(value)
            value +=1
        return result
```

