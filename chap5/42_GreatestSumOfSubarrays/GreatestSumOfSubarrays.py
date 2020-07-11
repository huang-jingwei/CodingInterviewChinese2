import random


#函数功能：找到数组的连续子数组最大和

# 基于思想：对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对整体和是有贡献的。
# 如果前几项累计值负数，则认为有害于总和，total记录当前值。
# 此时 若和大于maxSum 则用maxSum记录下来。最后返回maxSum。
#算法时间复杂度O（n）
def GetLeastNumbers(array):
    if array==None or len(array)<=0: #对数组进行判空操作
        return None
    elif len(array)==1:                  #数组只有一个元素时，直接返回该元素数值
        return array[0]
    total =array[0]                      #初始化当前子数组总和数值
    maxSum=array[0]                      #初始化连续子数组最大和
    for index in range(1,len(array)):    #遍历数组
        if total>=0:
            total=total+array[index]
        else:
            total=array[index]
        if total>=maxSum:
            maxSum=total
    return maxSum
######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=-20,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

#函数功能：采用穷举的方法找到连续子数组的最大和
#算法复杂度：O(N^2)
def GetLeastNumbers_right(array):
    if array==None or len(array)<=0:   #对数组进行判空操作
        return None
    elif len(array)==1:               #数组只有一个元素时，直接返回该元素数值
        return array[0]
    maxSubArraySum=array[0]           #连续子数组最大和
    for i in range(len(array)):
        count=0                       #记录从下标i所有可能的连续子数组的和
        for j in range(i,len(array)):
            count=count+array[j]
            if count>=maxSubArraySum:
                maxSubArraySum=count
    return maxSubArraySum

if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找出连续子数组的最大和
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                       # 随机数列表的长度
        array = randomList(length)         # 生成随机数列表
        right=GetLeastNumbers_right(array) # 对数器模块代码，用来做对比组
        test=GetLeastNumbers(array)        # 自己编写的代码模块，需要测试的代码模块
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))