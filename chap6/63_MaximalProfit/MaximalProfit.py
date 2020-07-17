import random

# 函数功能：递归
# 算法时间复杂度：O(N)
def Accumulate(number):
    return number>=1 and number+Accumulate(number-1)
######################下面代码是测试模块代码##################################

# 函数功能： 找出股票的最大利润
#基本思路：暴力解法，算法时间复杂度O(N^2)
# 搜索当前时间节点后的全部节点，找出股票收入最大的节点。
# 然后拿股票收入最大与当前的收入做比较，若比当前股票收入大，那么就产生利润，
# 并且此时的利润为最大利润。否则不交易股票，不产生利润。
def MaximalProfit_right1(array):
    if array==None or len(array)<2:
        return 0
    maxProfit=0
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[j]-array[i]>=maxProfit:
                maxProfit=array[j]-array[i]
    return maxProfit


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