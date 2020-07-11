# 面试题49：丑数

【题目】 把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第N个丑数。

例如：例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。



牛客网OJ：[丑数](https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)



**思路一：暴力解法**

最简单直接的方法，就是**逐个判断每个整数是不是丑数**，循环所有数字，判断它是不是丑数 首先我们需要判断某个整数number是不是丑数



先判断一个数是否是丑数

```Python
#函数功能：判断一个数是否是丑数
#丑数的定义： 把只包含因子2、3和5的数称作丑数（Ugly Number）
def IsUglyNumber(number):
    while number%5==0:
        number=number/5
    while number%3==0:
        number=number/3
    while number%2==0:
        number=number/2
    return (number==1)
```

再按照顺序，从头开始寻找第n个丑数，代码如下

```python
#函数功能：按从小到大的顺序的第N个丑数
#基本思路：采用遍历的方式,找出第N个丑数
def UglyNumber_right(n):
    if n<=0:                             #判断输入是否为空
        return None
    count=0                              #计数器，用来这是第几个丑数
    number=1                             #丑数的第一位默认为1
    while count<n:
        if IsUglyNumber(number)==True:   #如果是丑数，计算器加1
            count=count+1
        if count==n:                     #找到第n个丑数
            return number
        number=number+1
```

这个算法很简单，但是最大的问题是每个整数都需要进行计算。即使一个数字不是丑数，我们还是需要对他进行求余数和除法操作。





**思路二：结合丑数的特性**

**根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。**   因此我们可以创建一个数组，里面的数字是排好序的丑数。里面的每一个丑数是前面的丑数乘以2、3或者5得到的。**那关键就是确保数组里的丑数是有序的了。**



现在我们来生成下一个丑数，该丑数肯定是前面某一个丑数乘以2、3或者5的结果。 我们首先考虑把已有的每个丑数乘以2。在乘以2的时候，能得到若干个结果小于或等于M的。由于我们是按照顺序生成的，小于或者等于M肯定已经在数组中了，我们不需再次考虑； 我们还会得到若干个大于M的结果，但我们只需要第一个大于M的结果，因为我们希望丑数是按从小到大顺序生成的，其他更大的结果我们以后再说。 我们把得到的第一个乘以2后大于M的结果，记为M2。同样我们把已有的每一个丑数乘以3和5，能得到第一个大于M的结果M3和M5。 **那么下一个丑数应该是M2、M3和M5三个数的最小者。**



```python
#函数功能：按从小到大的顺序的第N个丑数
def UglyNumber(n):
    if n <= 0:             # 判断输入是否为空
        return None
    uglyNum=[1]*n          #生成一个数组来存放丑数，丑数的第一位默认为1
    count=1                #计数器，用来这是第几个丑数
    index2 = 0
    index3 = 0
    index5 = 0
    while count<n:
        #竞争产生下一个丑数
        uglyValue=min(uglyNum[index2]*2,uglyNum[index3]*3,uglyNum[index5]*5)
        if uglyValue == uglyNum[index2]*2: #将产生这个丑数的index*向后挪一位
            index2=index2+1
        if uglyValue== uglyNum[index3]*3:  #这里不能用elseif，因为可能有两个最小值，这时都要挪动；
            index3=index3+1
        if uglyValue == uglyNum[index5]*5:
            index5=index5+1
        uglyNum[count] = uglyValue #更新丑数数组
        count=count+1              #计数器加1
    return uglyNum[n-1]
```









