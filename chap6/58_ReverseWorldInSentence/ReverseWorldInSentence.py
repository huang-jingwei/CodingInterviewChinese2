#函数功能：翻转字符串
#解题思路：翻转字符串本质上就是字符串的左侧右侧对应位置相互交换元素

class Solution:
    def reverseWords(self, s: str) -> str:
        if s == None:
            return s

        stringList = s.strip().split()          # 去掉字符串的头尾空格，已经字符串间以空格划分
        leftIndex = 0                           # 字符串左侧元素指针，从头节点开始
        rightIndex = len(stringList) - 1        # 字符串右侧元素指针，从尾节点开始
        while leftIndex < rightIndex:           # 交换字符串左侧右侧对应位置元素
            stringList[leftIndex], stringList[rightIndex] = stringList[rightIndex], stringList[leftIndex]
            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1
        string = ""
        for index in range(len(stringList)):   # 将翻转后字符串拼接起来
            if index != len(stringList) - 1:
                string = string + stringList[index] + " "
            else:
                string = string + stringList[index]
        return string