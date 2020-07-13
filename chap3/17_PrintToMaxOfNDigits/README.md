# 面试题17：打印从1到最大的n位数



【题目】输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。



LeetCode:[打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)



说明：

- 用返回一个整数列表来代替打印
- n 为正整数



**思路一：暴力解法**



```Python
def PrintToMaxOfNDigits(n):
    number = 1                      # 初始化数值number，代表所生成的正整数
    array = []                      # 初始化一个数组，用来存放所有生成的正整数
    while number < 10 ** n:
        array.append(number)
        number = number + 1
    return array
```

