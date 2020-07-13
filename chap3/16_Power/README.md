# 面试题16：数值的整数次方



【题目】实现函数double Power(double base,int exponent)。求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。



LeetCode:[数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)



指数幂的所有边界包括

- 指数为0的情况，不管底数是多少都应该是1
- 指数为负数的情况，求出的应该是其倒数幂的倒数
- 指数为负数的情况下，底数不能为0





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











