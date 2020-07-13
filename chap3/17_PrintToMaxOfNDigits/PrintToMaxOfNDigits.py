
# 函数功能：打印从1到最大的n位数
# 说明
# - 用返回一个整数列表来代替打印
# - n 为正整数
def PrintToMaxOfNDigits(n):
    number = 1                      # 初始化数值number，代表所生成的正整数
    array = []                      # 初始化一个数组，用来存放所有生成的正整数
    while number < 10 ** n:
        array.append(number)
        number = number + 1
    return array