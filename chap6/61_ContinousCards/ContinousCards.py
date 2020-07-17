import random

# 函数功能：递归
# 算法时间复杂度：O(N)
def Accumulate(number):
    return number>=1 and number+Accumulate(number-1)
######################下面代码是测试模块代码##################################

# 函数功能： 求1+2+...+n
# 基本思路：直接相加
# 算法时间复杂度：O(N)
def Accumulate_right1(number):
    if number== None or number==0:      # 若输入数组为空，直接输出0
        return 0
    count = 0                           # 初始化计数器，用来记录总和
    for i in range(number+1):
        count=count+i
    return count


# 函数功能： 求1+2+...+n
# 基本思路：等差数列的求和公式sum=(a1+an)*n/2
# 算法时间复杂度：O(N)
def Accumulate_right2(number):
    if number== None or number==0:       # 若输入数组为空，直接输出0
        return 0
    return int((1+number)*number/2)


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找到数组中的逆序对个数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        number = random.randint(0,100)                   # 生成一个随机数
        right =Accumulate_right1(number)                  # 对照组实验，思路一
        test = Accumulate(number)                       # 改进后算法，思路二
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))