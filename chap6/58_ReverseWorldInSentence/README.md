# 面试题58：翻转字符串



【题目一】输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。



**例如**

```python
输入: "the sky is blue"
输出: "blue is sky the"

    
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

    
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。   
```



LeetCode:[翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/)



**解题思路**

翻转字符串本质上就是字符串的左侧右侧对应位置相互交换元素。

```Python
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
```



【题目二】字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。





**例如**

```Python
输入: s = "abcdefg", k = 2
输出: "cdefgab"
```



```python
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
```



LeetCode:[翻转左侧字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

**解题思路**

解法一：一种比较暴力的方法，分别将字符串中左右对应位置的元素提取出来，再进行重新拼接

```Python
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
```







