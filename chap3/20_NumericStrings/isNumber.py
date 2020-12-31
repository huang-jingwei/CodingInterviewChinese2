class Solution:
    def isNumber(self, s: str) -> bool:
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 阿拉伯数组
        exp_string = ["e", "E"]                                   # 表示指数部分的字符
        point = ["."]                                             # 表达小数点
        attribute = ["+", "-"]                                    # 正负号

        # step1:将字符串转化为有效字符列表，去掉字符串首尾两端的空格
        string = list(s)  # 将字符串转化为字符串列表
        while len(string) > 0 and string[-1] == " ":
            string.pop()
        while len(string) > 0 and string[0] == " ":
            string.pop(0)
        length = len(string)

        # step2: 进行字符串判断
        # 情况1：只有一个字符时，该字符必须为数字字符
        if length == 1:
            if string[0] not in num:
                return False

        # 情况2：若字符串存在指数字符("e","E"),则字符后面不能存在小数点、其他字符
        # 若正负号字符存在，则只能存在指数字符的后一位，且不能是最后一位
        e_index = None
        for index in range(length):
            if string[index] in exp_string:
                e_index = index
                break

        if e_index != None:
            if e_index == length - 1 or e_index == 0:
                return False
            else:
                # 指数部分的字符("e","E")只能存在数字和正负号
                for index in range(e_index + 1, length):
                    if string[index] in attribute:
                        if index != e_index + 1 or index == length - 1:
                            return False
                    else:
                        if string[index] not in num:
                            return False

        # 情况3：若字符串存在指数字符("e","E")，若不存在指数字符，则将字符长度视作指数字符下标
        # 指数字符前面只能存在小数点、数字
        if e_index == None:
            e_index = length

        # 小数点只能出现一次，且不能在首部
        # 正负号只能出现一次，只能在首部
        pointNum = 0      # 小数点计算器
        isNumber = False  # 判断指数字符前面是否存在数字
        for index in range(e_index):
            if string[index] in attribute:
                if index != 0:
                    return False
            elif string[index] in point:
                pointNum += 1
                if pointNum > 1:
                    return False
            else:
                if string[index] not in num:
                    return False
                else:
                    isNumber = True

        if length == 0 or isNumber == False:  # 空字符或者不存在数字
            return False
        else:
            return True     