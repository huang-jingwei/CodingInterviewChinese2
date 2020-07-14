import random

# 函数功能： 找出数组中和为s的两个数字
# 基本思路：等差数列的求和公式sum=(a1+an)*n/2
# 算法时间复杂度：O(N)
def TwoNumbersWithSum(array,s):
    if array== None or len(array)==0:     # 若输入数组为空，直接输出0
        return False
    data={}                               # 初始化一个字典，模拟哈希表，用来存放数组的数值
    for index in range(len(array)):       # 在哈希表中，key：数组中元素，value：该元素在数组中第一次出现时对应的下标
        if array[index] not in data:
            data[array[index]]=index
    for key,value in data.items():        # 遍历哈希表
        if s-key in data:
            return [key,s-key]


# 函数功能： 找出数组中和为s的两个数字
# 基本思路：最简单直接的方法就是直接遍历数组
# 算法时间复杂度：O(N^2)
def TwoNumbersWithSum_right(array,s):
    if array== None or len(array)==0:     # 若输入数组为空，直接输出0
        return False
    for index in range(len(array)):       # 遍历数组
        for anotherIndex in range(len(array)):
            if array[index]+array[anotherIndex]==s and index!=anotherIndex:
                return [array[index],array[anotherIndex]]
