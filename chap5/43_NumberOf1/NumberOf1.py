import random


#函数功能：1到n整数中1出现的次数

# 基于思想：对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对整体和是有贡献的。
# 如果前几项累计值负数，则认为有害于总和，total记录当前值。
# 此时 若和大于maxSum 则用maxSum记录下来。最后返回maxSum。
#算法时间复杂度O（n）
def NumberOf1(n):
    pass




######################下面代码是测试模块代码##################################

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

if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找出1到n整数中1出现的次数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        number = random.randint(0,500)      # 在0~500范围内，随机生成一个整数
        right=NumberOf1_right(number)       # 对数器模块代码，用来做对比组
        test=NumberOf1(number)              # 自己编写的代码模块，需要测试的代码模块
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))

