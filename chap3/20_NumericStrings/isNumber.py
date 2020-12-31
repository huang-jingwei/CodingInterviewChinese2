
# 函数功能：调整数组顺序使奇数位于偶数前面
# 基本思路：借鉴荷兰国旗问题的解法
def ReorderArray(array):
    if array==None or len(array)==0:    # 输入为空数组时，直接输出
        return array
    more=len(array)                     # 数组中，下标≥more的位置均为偶数
    index = 0                           # 初始化移动下标
    while index<more:
        if array[index]%2==1:           # 该位置元素为奇数时，移动下标右前进一位
            index=index+1
        else:                           # 该位置元素为偶数时，more减一，当前位置与more位置交换元素
            more=more-1                 # 注意此时index不可右前进一位，因为并不知道新交换过来的数值的奇偶性
            array[index],array[more]=array[more],array[index]
    return array