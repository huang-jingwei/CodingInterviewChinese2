import random


#函数功能：计算数值的整数次方
#基本思路：对幂次运算进行优化
def Power(base,exponent):
    if exponent==0:                                   # 幂次为零时
        if base!=0:                                   # 若底数不为0，返回1，反之报错
            return 1
        else:
            return False
    elif exponent>0:                                  # 幂次为正数时
        result = PowerUnsignedExponent(base,exponent) # 调用函数计算数值的幂次
        return result
    elif exponent<0:                                 # 幂次为负数时
        item=-exponent                               # 先将指数取绝对值
        result = PowerUnsignedExponent(base,item)    #先调用函数计算数值的正数幂次
        if result==0:                                # 再对所得数取倒数
            return False
        else:
            return 1/result

#假设底数非0且幂次都是非负数时，对数值进行幂次运算
#基本思路：采用递归的方式对幂次进行简化
def PowerUnsignedExponent(base,exponent):
    if exponent==0:                                 # 幂次为0时，返回1
        return 1
    if exponent==1:                                 # 幂次为1时，返回底数
        return base
    result=PowerUnsignedExponent(base,exponent//2)  # 采用递归对幂次运算进行加速运算
    result=result*result
    if exponent%2==1:
        result=result*base
    return result

######################下面代码是测试模块代码##################################

# 函数功能：求数值的整数次方
# 基本思路：暴力解法,直接求base的exponent次方
def Power_right(base,exponent):
    if exponent==0:          # 幂次为零时
        if base!=0:          #若底数不为0，返回1，反之报错
            return 1
        else:
            return False
    elif exponent>0:        # 幂次为正数时
        count = 1           # 初始化计数器，用来记录数值的整数次方
        for i in range(exponent):
            count = count * base
        return count
    elif exponent<0:       # 幂次为负数时
        item=-exponent     # 先将指数取绝对值
        count = 1          # 初始化计数器，用来记录数值的整数次方
        for i in range(item):
            count = count * base
        if count==0:      # 再对所得数取倒数
            return False
        else:
            return 1/count


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,计算数值的整数次方
    errorCount = 0                         # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        length = 500                       # 随机数列表的长度
        base = random.randint(-200,500)    # 生成两个随机数
        exponent=random.randint(0,1000)
        right =Power_right(base,exponent)  # 对照组实验，思路一:暴力解法
        test = Power(base,exponent)        # 改进后算法，思路二
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))