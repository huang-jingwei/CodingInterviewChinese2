# 面试题63：股票的最大利润

【题目】 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

【例如】

```python
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```



```Python
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

```





LeetCode:[股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

**思路一：暴力解法**

最简单直接的方法就是搜索当前时间节点后的全部节点，找出股票收入最大的节点。然后拿股票收入最大与当前的收入做比较，若比当前股票收入大，那么就产生利润，并且此时的利润为最大利润。否则不交易股票，不产生利润。

算法时间复杂度：O(N^2)

```Python
# 函数功能： 找出股票的最大利润
#基本思路：暴力解法，算法时间复杂度O(N^2)
# 搜索当前时间节点后的全部节点，找出股票收入最大的节点。
# 然后拿股票收入最大与当前的收入做比较，若比当前股票收入大，那么就产生利润，
# 并且此时的利润为最大利润。否则不交易股票，不产生利润。
def MaximalProfit_right1(array):
    maxProfit=0
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[j]-array[i]>=maxProfit:
                maxProfit=array[j]-array[i]
    return maxProfit
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



