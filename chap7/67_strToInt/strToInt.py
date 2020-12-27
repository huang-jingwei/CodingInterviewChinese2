class Solution:
    def myAtoi(self, s: str) -> int:
        # 创建有效数组，即10个阿拉伯数组和正负号
        valid = {"+": 1, "-": 1}
        for index in range(10):
            valid[str(index)] = 1

        # step1:去掉字符串首尾的空字符，再将其转化为字符列表
        string = list(s.strip())
        right = len(string)

        # step2:确定字符组合区间的右下标
        for index in range(len(string)):
            if string[index] not in valid:  # 第一个无效字符
                right = index
                break
            elif string[index] in ["+", "-"] and index != 0:  # +，-号只能出现在字符串首部
                right = index
                break
        # 字符组合区间中字符个位为0，即不可能组成有效字符，直接返回0
        if right == 0:
            return 0

        # step3：拼接字符
        value = ""
        attribute = 1  # 字符的正负性
        for index in range(right):
            if index == 0:
                # 首字符是正负号
                if string[index] == "+":
                    attribute = 1
                elif string[index] == "-":
                    attribute = -1
                else:
                    value += string[index]
            else:
                value += string[index]
        if value == "":
            return 0
        value = attribute * int(value)

        # step4:判断数组是否在输出数值范围内
        if value >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif value <= -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return value