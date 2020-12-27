# 面试题67：把字符串转换成整数



【题目】写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

 

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31− 1]。如果数值超过这个范围，请返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。

**示例 :**

```python
输入: "42"
输出: 42

    
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。  
    
    
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
        
        
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−2^31) 。
```



LeetCode:[字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)





```Python
class Solution:
    def myAtoi(self, s: str) -> int:
        # 创建有效数组，即10个阿拉伯数组和正负号
        valid={"+":1,"-":1}
        for index in range(10):
            valid[str(index)]=1
        
        # step1:去掉字符串首尾的空字符，再将其转化为字符列表
        string=list(s.strip())
        right=len(string)

        # step2:确定字符组合区间的右下标
        for index in range(len(string)):
            if string[index] not in valid:               # 第一个无效字符         
                right=index
                break
            elif string[index]in ["+","-"] and index!=0: # +，-号只能出现在字符串首部
                right=index
                break
        # 字符组合区间中字符个位为0，即不可能组成有效字符，直接返回0
        if right==0:   
            return 0

    
        # step3：拼接字符
        value=""
        attribute=1   #字符的正负性
        for index in range(right):
            if index==0:
                # 首字符是正负号
                if string[index] =="+":
                    attribute=1
                elif  string[index] =="-":
                    attribute=-1
                else:
                    value +=string[index]
            else:
                value +=string[index]
        if value=="":
            return 0   
        value=attribute*int(value)

        # step4:判断数组是否在输出数值范围内
        if value>=2**31-1:
            return 2**31-1
        elif value<=-1*2**31:
            return -1*2**31
        else:
            return value
```



