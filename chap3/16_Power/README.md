# 面试题16：数值的整数次方



【题目】实现函数double Power(double base,int exponent)。求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。



LeetCode:[数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)



**思路一：暴力解法**



```Python
# 函数功能：求数值的整数次方
# 基本思路：暴力解法,直接求base的exponent次方
def Power_right(base,exponent):
    if exponent==0:            # 若是零次方，直接返回1
        return 0
    count = 1                  # 初始化计数器，用来记录数值的整数次方
    for i in range(exponent):
        count=count*base
    return count
```











