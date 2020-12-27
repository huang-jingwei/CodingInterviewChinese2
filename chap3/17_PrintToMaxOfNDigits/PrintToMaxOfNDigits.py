
# 函数功能：打印从1到最大的n位数
# 说明
# - 用返回一个整数列表来代替打印
# - n 为正整数
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result=[]
        value=1
        while value<10**n:
            result.append(value)
            value +=1
        return result