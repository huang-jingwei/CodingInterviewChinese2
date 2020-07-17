class Solution:
    def hammingWeight(self, n: int) -> int:
        n=abs(n)                     # 现将输入数字转为非负数
        index=0                      # 二进制的移动光标
        count=0                      # 计数器，用来记录二级制转化中数位为1的个数
        while 2**index <=n:
            num=int(n/2**index %2)   # 二级制转化后，当前数值
            if num==1:               # 若该数值为1，计数器加一
                count=count+1
            index=index+1
        return count