#函数功能：翻转字符串，对应题目一
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
        for index in range(len(stringList)):    # 将翻转后字符串拼接起来
            if index != len(stringList) - 1:
                string = string + stringList[index] + " "
            else:
                string = string + stringList[index]
        return string

#函数功能：左旋转字符串，对应题目二
#解题思路：一种比较暴力的方法，分别将字符串中左右对应位置的元素提取出来，再进行重新拼接
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if s == None:                      #对输入字符串进行判空
            return None
        stringList = []                    #将输入字符串每个位置的字符用列表结构存储起来
        for index in range(len(s)):
            stringList.append(s[index])

        leftArray = stringList[:n]        #分别将字符串中左右对应位置的元素提取出来
        rightArray = [""]
        if n <= len(stringList) - 1:
            rightArray = stringList[n:]

        string = ""                      #将上诉所得字符元素进行重新拼接
        for index in range(len(rightArray)):
            string = string + rightArray[index]

        for index in range(len(leftArray)):
            string = string + leftArray[index]

        return string