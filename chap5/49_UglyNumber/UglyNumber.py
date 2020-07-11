import random


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

######################下面代码是测试模块代码##################################
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


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找出从小到大的顺序的第N个丑数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(5000):
        n = random.randint(0,500)          # 生成一个随机整数
        right=UglyNumber_right(n)          # 对数器模块代码，用来做对比组
        test=UglyNumber(n)                 # 自己编写的代码模块，需要测试的代码模块
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))