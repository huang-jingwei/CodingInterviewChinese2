# 面试题46：把数字翻译成字符串

**题目描述：** 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



```python
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```



LeetCode:[把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)



采用动态规划的方法进行求解

```python
class Solution:
    def translateNum(self, num: int) -> int:
        # 将数字类型数据转化为列表形式
        string = str(num)
        dataArray = [int(string[index]) for index in range(len(string))]

        # 初始化列表，waysCount[i]:代表从0~i长度列表的解码方法总数
        # 对比与dataArray列表，waysCount增加了一位，waysCount[0]记录字符串为空时的解码方法
        waysCount = [0] * (len(dataArray) + 1)
        waysCount[0] = 1                        # 空字符有1种解码方式

        for index in range(1, len(waysCount)):  # 依次遍历各个字符

            # 只有数字在0~25之间才能进行解码
            # 基于上面的分析，个位数要在0~9之间，双位数要在0~25之间
            if dataArray[index - 1] >= 0:
                waysCount[index] = waysCount[index - 1]

            # num为当前位置和前一位数字组成的双位数
            if index - 2 >= 0 and dataArray[index - 2] != 0:
                num = dataArray[index - 2] * 10 + dataArray[index - 1]
                if 0 <= num and num <= 25:
                    waysCount[index] += waysCount[index - 2]
        return waysCount[-1]
```





