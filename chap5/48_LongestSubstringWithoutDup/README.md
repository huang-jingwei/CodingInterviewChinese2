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

先将字符串数据转化为列表格式

1、初始化一个哈希表indexData，用来存放遍历过程中所出现的字符的索引位置

2、然后再初始化两个移动下标left=right=0，分别为子字符串的左右边界

3、right移动下标从左向右对字符列表数据进行遍历  

 (注意，在移动过程中，left和right移动指针只会向右移动，不会回退)



- 遍历的字符在之前没有出现过，right继续向右移动，加 1。
- 遍历的字符在之前出现过，判断重复的字符的下标index是否在该段字符的区间内（即left<=index<=right)。若不在区间内，更新这个字符的下标，right继续向右移动，加 1；若在区间内，更新字符串的左下标left。

在上面的遍历过程中，每移动一步都更新不重复子序列的最长长度



算法时间复杂度为：O(N)

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











