# 面试题48：最长不含重复字符的子字符串



【题目】 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



**示例** 

```python
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```



```python
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```



LeetCode:[最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)



**思路：左右移动指针**



```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 将字符串数据转化为列表类型数据
        string = [s[index] for index in range(len(s))]

        if len(string) == 0:        # 输入为空字符串时，子字符串长度为0
            return 0

        indexData = {}              # 存放各个字符串的下标索引
        maxLength = float("-inf")   # 不重复的子字符串的最长长度

        left = 0                    # left,right分别为子字符串的左右边界
        right = 0

        while right < len(string):

            # string[right]在该段子字符串还未出现过，则右指针继续向前移动
            # 每移动一步，都更不重复子字符串的最长长度
            if string[right] not in indexData:
                indexData[string[right]] = right
                maxLength = max(maxLength, right - left + 1)
                right += 1

            else:
                # string[right]字符已经在之前出现过
                # 判断该字符串是在这段子字符串出现重复字符，还是在之前的子序列出现
                index = indexData[string[right]]

                # 若是在之前的子序列出现，则更新坐标
                # 否则更新子序列的左右边界
                if index < left:
                    indexData[string[right]] = right
                    maxLength = max(maxLength, right - left + 1)  # 每移动一步，都更不重复子字符串的最长长度
                    right = right + 1
                else:
                    maxLength = max(maxLength, right - left)      # 这段子字符串已经出现重复字符，左指针开始移动
                    left = index + 1
        return maxLength
```











