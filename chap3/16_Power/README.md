# 面试题16：数值的整数次方



【题目】实现函数double Power(double base,int exponent)。求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。



LeetCode:[数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)



指数幂的所有边界包括

- 指数为0的情况，不管底数是多少都应该是1
- 指数为负数的情况，求出的应该是其倒数幂的倒数
- 指数为负数的情况下，底数不能为0



```Python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:       # 幂次为零时                   
            if x!=0:   # 若底数不为0，返回1，反之报错        
                return 1
            else:
                return False
        elif n>0:      # 幂次为正数时          
            result = self.PowerUnsignedExponent(x,n)   # 调用函数计算数值的幂次
            return result
        elif n<0:                                      # 幂次为负数时
            item=-n                                    # 先将指数取绝对值
            result = self.PowerUnsignedExponent(x,item)#先调用函数计算数值的正数幂次
            if result==0:                              # 再对所得数取倒数
                return False
            else:
                return 1/result
    
    #假设底数非0且幂次都是非负数时，对数值进行幂次运算
    #基本思路：采用递归的方式对幂次进行简化
    def PowerUnsignedExponent(self,base,exponent):
        if exponent==0:                                      # 幂次为0时，返回1
            return 1
        if exponent==1:                                      # 幂次为1时，返回底数
            return base
        result=self.PowerUnsignedExponent(base,exponent//2)  # 采用递归对幂次运算进行加速运算
        result=result*result
        if exponent%2==1:
            result=result*base
        return result
```

