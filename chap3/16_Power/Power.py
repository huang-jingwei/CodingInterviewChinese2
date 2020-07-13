import random


#函数功能：找到数组中的逆序对个数
#基本思路：还未完全实现
def Power(base,exponent):
    if exponent==0:            # 若是零次方，直接返回1
        return 0
    pass

######################下面代码是测试模块代码##################################

# 函数功能：求数值的整数次方
# 基本思路：暴力解法,直接求base的exponent次方
def Power_right(base,exponent):
    if exponent==0:            # 若是零次方，直接返回1
        return 0
    count = 1                  # 初始化计数器，用来记录数值的整数次方
    for i in range(exponent):
        count=count*base
    return count


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找到数组中的逆序对个数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                       # 随机数列表的长度
        base = random.randint(-200,500)    # 生成两个随机数
        exponent=random.randint(0,100)
        right =Power_right(base,exponent)  # 对照组实验，思路一:暴力解法
        test = Power(base,exponent)        # 改进后算法，思路二
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))