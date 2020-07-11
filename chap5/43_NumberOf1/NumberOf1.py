
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


