# 面试题10：斐波那契数列



**题目一：求斐波那契数列的第n项**

牛客网OJ：[斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-rankingg)



递推公式f(n) =​

- f(n)=0, 当n=0​时
- f(n)=1, 当n=1时
- f(n)=f(n - 1) + f(n - 2), 其他情形



牛客网OJ：[斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-rankingg)



递归方法实现：算法复杂度O（2^N）

循环方法实现：算法复杂度O（N）



```python
#函数功能：斐波那契数列,输出数列的第k项
#算法复杂度:O(N)

def Fibonacci(k):
    if k<0:            #k为非负整数，当输入的k为负数时，直接输出false
        return False
    if k==0:           #当k=0、1时，直接输出对应数值
        return 0
    elif k==1:
        return 1
    else:              #当k>1时，采用数组形式来记录斐波那契数列数值
        array=[0]*(k+1)
        array[1]=1
        for index in range(2,len(array)):
            array[index]=array[index-1]+array[index-2]
        return array[k]
```



**题目二：青蛙台阶问题**

【题目】一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

【分析】
每次只能跳一级或者跳两级，那么调N个台阶就可以分解为

先跳1级，然后剩余的是跳一个N - 1​级的台阶，

先跳2级，然后剩余的是跳一个N - 2​级的台阶，

以此类推，那么它的递推公式为

- f(n)=0, 当n=0时
- f(n)=1, 当n=1时
- f(n)=2, 当n=2时
- f(n)=f(n - 1) + f(n - 2), 其他情形时



递归方法实现：算法复杂度O（2^N）

循环方法实现：算法复杂度O（N）



```python
#函数功能：斐波那契数列,输出数列的第k项
#算法复杂度:O(N)

def Fibonacci(k):
    if k<0:            #k为非负整数，当输入的k为负数时，直接输出false
        return False
    if k==0:           #当k=0、1、2时，直接输出对应数值
        return 0
    elif k==1:
        return 1
    elif k==2:
        return 2
    else:              #当k>1时，采用数组形式来记录斐波那契数列数值
        array=[0]*(k+1)
        array[1]=1
        array[2]=2
        for index in range(2,len(array)):
            array[index]=array[index-1]+array[index-2]
        return array[k]
```

