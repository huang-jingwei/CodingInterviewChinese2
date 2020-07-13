import random


# 函数功能： 统计一个数字在排序数组中出现的次数
# 基本思路：因为该数组是有序数组，因此采用二分查找的方法进行缩小搜索区间
# 算法时间复杂度：O(log N)
def NumberOfK(array,k):
    if array== None or len(array)==0:  # 若输入数组为空，直接输出0
        return 0
    left=0                             # 初始化搜索区间的左右边间
    right=len(array)-1
    while left<right:
        mid = left+(right-left)//2     # 搜索区间的中间点,防止溢出
        if array[mid]==k:
            break
        elif array[mid]<k:
            left=mid+1
        elif array[mid]>k:
            right=mid
    if array[mid]!=k:                  # 若不是array[mid]==k跳出循环，则说明数组中不存在k
        return 0
    #此时得到array[mid]==k，再以下标mid左右展开进行搜索
    #找出数组array中数值等于k的区间左右下标
    leftIndex=mid
    rightIndex=mid
    while leftIndex-1>=0 and array[leftIndex-1]==k:
        leftIndex=leftIndex-1
    while rightIndex+1<=len(array)-1 and array[rightIndex+1]==k:
        rightIndex=rightIndex+1

    count=rightIndex-leftIndex+1
    return count

######################下面代码是测试模块代码##################################

#生成指定长度的随机数列表
#参数说明:length:列表长度，low，high：分别为随机数列表数值的范围
def randomList(length,low=0,high=100):
    array=[]
    for i in range(length):
        array.append(random.randint(low,high))
    return array

# 函数功能： 统计一个数字在排序数组中出现的次数
# 基本思路：遍历数组array来进行统计数字k出现的次数
# 算法时间复杂度：O(N)
def NumberOfK_right(array,k):
    if array== None or len(array)==0:       # 若输入数组为空，直接输出0
        return 0
    count = 0                               # 初始化计数器，用来记录数字k在数组array中出现的次数
    for index in range(len(array)):         # 遍历数组
        if array[index]==k:
            count=count+1
    return count


if __name__=="__main__":

    # 采用对数器方法进行对所写代码进行验证,找到数组中的逆序对个数
    errorCount = 0  # 记录测试过程中算法求解错误的次数
    for i in range(10000):
        k = random.randint(0,100)                        # 生成一个随机数
        array =  randomList(length=300,low=-20,high=100) # 生成随机数列表
        right =NumberOfK_right(array,k)                  # 对照组实验，思路一
        test = NumberOfK(array,k)                        # 改进后算法，思路二
        if right == test:
            print("第%d次测试：测试准确" % (i))
        else:
            print("第%d次测试：测试错误" % (i))
            errorCount = errorCount + 1
    print("测试过程中算法求解错误的次数%d" % (errorCount))