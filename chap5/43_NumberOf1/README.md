# 面试题43：1到n整数中1出现的次数

**题目描述：** 输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。

例如：输入12,1~12这些整数中包含1的数字有1、10、11、12,1一共出现了5次



牛客网OJ：[从1到n整数中1出现的次数](https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?tpId=13&tqId=11184&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)



**思路一：暴力解法**

最简单直接的方法就是我们循环所有的1~n中的每个number，计算每个number中数字1出现的次数。

算法时间复杂度：O(N *logN)



判断一个数是否含有数字1，可以通过下述代码来得到

```Python
#函数功能：计算数字number中数字1出现的总次数
#算法复杂度：O(logN)
def NumberTimesOf1(number):
    if number==None:                  #输入为空时，直接返回0
        return 0
    times=0                            #记录数字number中数字1出现的次数
    index=0                            #十进制的位数
    while 10**index<=number:
        item=int(10/(10**index))%10    #获得数字在十进制下的每个位置的数字
        if item==1:                    #若该位置上数字为1，计算器加1
            times=times+1
        index=index+1
    return times
```

在上述代码中，对每个数字都要做除法和求余运算，以求出该数字中1出现的次数。如果输入数字n，n有log n位。因此我们需要判断n个数字时，总的算法时间复杂度为O(N *logN)。



```python
#函数功能：1到n整数中1出现的次数
#基本思路：采用遍历的方式,找出在区间范围内元素中数字1出现的总个数
#算法复杂度：O(N *logN)
def NumberOf1_right(n):
    if n==None or n==0:                    #判断输入是否为空
        return 0
    count=0                                #计数器，用来记录数字1出现的总次数
    for number in range(n):
        count=count+NumberTimesOf1(number) #记录数组每个元素中数字1出现的总次数
    return count

#函数功能：计算数字number中数字1出现的总次数
#算法复杂度：O(logN)
def NumberTimesOf1(number):
    if number==None:                  #输入为空时，直接返回0
        return 0
    times=0                            #记录数字number中数字1出现的次数
    index=0                            #十进制的位数
    while 10**index<=number:
        item=int(10/(10**index))%10    #获得数字在十进制下的每个位置的数字
        if item==1:                    #若该位置上数字为1，计算器加1
            times=times+1
        index=index+1
    return times
```









