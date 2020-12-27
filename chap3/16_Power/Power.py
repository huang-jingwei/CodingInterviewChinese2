class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:  # 幂次为零时
            if x != 0:  # 若底数不为0，返回1，反之报错
                return 1
            else:
                return False
        elif n > 0:  # 幂次为正数时
            result = self.PowerUnsignedExponent(x, n)  # 调用函数计算数值的幂次
            return result
        elif n < 0:  # 幂次为负数时
            item = -n  # 先将指数取绝对值
            result = self.PowerUnsignedExponent(x, item)  # 先调用函数计算数值的正数幂次
            if result == 0:  # 再对所得数取倒数
                return False
            else:
                return 1 / result

    # 假设底数非0且幂次都是非负数时，对数值进行幂次运算
    # 基本思路：采用递归的方式对幂次进行简化
    def PowerUnsignedExponent(self, base, exponent):
        if exponent == 0:  # 幂次为0时，返回1
            return 1
        if exponent == 1:  # 幂次为1时，返回底数
            return base
        result = self.PowerUnsignedExponent(base, exponent // 2)  # 采用递归对幂次运算进行加速运算
        result = result * result
        if exponent % 2 == 1:
            result = result * base
        return result