import random


#函数功能：找到数组中的逆序对个数
#基本思路：采用哈希表来存放字符出现的次数
# 算法时间复杂度：O(N)
def InversePairs(array):
    if array == None or len(array) == 0:  # 判断输入是否为空
        return 0
    pass

######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

# 函数功能：找到数组中的逆序对个数
# 基本思路：暴力搜索
# 每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对
# 算法时间复杂度：O(N^2)
def InversePairs_right(array):
    if array== None or len(array)==0:       # 判断输入是否为空
        return 0
    count = 0                               # 初始化计数器，用来记录逆序对的总个数
    for i in range(len(array)):             # 遍历数组
        for j in range(i+1,len(array)):
            if array[i]>array[j]:           # 找到逆序对，计数器加一
                count=count+1
    return count


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找到数组中的逆序对个数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                       # 随机数列表的长度
        array = randomList(length)         # 生成随机数列表
        right =InversePairs_right(array)   # 对照组实验，思路一
        test = InversePairs(array)         # 改进后算法，思路二
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))