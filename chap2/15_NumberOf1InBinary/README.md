# 面试题15：二进制中1的个数



【题目】请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。



**示例 1：**

```python
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

```





LeetCode:[二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)



```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        n=abs(n)                     # 现将输入数字转为非负数
        index=0                      # 二进制的移动光标
        count=0                      # 计数器，用来记录二级制转化中数位为1的个数
        while 2**index <=n:
            num=int(n/2**index %2)   # 二级制转化后，当前数值
            if num==1:               # 若该数值为1，计数器加一
                count=count+1
            index=index+1
        return count
```
























