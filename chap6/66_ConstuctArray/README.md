# 面试题64：求1+2+…+n

【题目一】 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。



LeetCode:[求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

**思路一：暴力解法**

最简单直接的方法就是将这n个数直接相加。

算法时间复杂度：O(N)

```Python
# 函数功能： 求1+2+...+n
# 基本思路：直接相加
# 算法时间复杂度：O(N)
def Accumulate_right1(number):
    if number== None or number==0:      # 若输入数组为空，直接输出0
        return 0
    count = 0                           # 初始化计数器，用来记录总和
    for i in range(number+1):
        count=count+i
    return count
```



**思路二：公式**

例如等差数列的求和公式

```python
# 函数功能： 求1+2+...+n
# 基本思路：等差数列的求和公式sum=(a1+an)*n/2
# 算法时间复杂度：O(N)
def Accumulate_right2(number):
    if number== None or number==0:       # 若输入数组为空，直接输出0
        return 0
    return int((1+number)*number/2)
```

**思路三：递归**

采用递归来模拟循环

```python
# 函数功能：递归
# 算法时间复杂度：O(N)
def Accumulate(number):
    return number>=1 and number+Accumulate(number-1)
```

