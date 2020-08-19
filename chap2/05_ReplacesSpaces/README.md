# 面试题5：替换空格

**【题目】：**  请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

例如：输入“We are happy.”,则输出““We%20are%20happy.”





LeetCode:[替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)





【解题思路】

解法一：先将字符串的各个元素都取出，放到数组中。对数组元素进行修改，再将修改后的元素拼接起来。

```python
#函数功能：把字符串 s 中的每个空格替换成"%20"
#解法一：利用Python数据结构的特性
#基本思路：先将字符串的各个元素都取出，放到数组中。对数组元素进行修改，再将修改后的元素拼接起来。
def ReplacesSpaces_right(s):
    array = [s[i] for i in range(len(s))]
    for i in range(len(array)):
        if array[i] == " ":
            array[i] = '%20'
    string = ""
    for i in range(len(array)):
        string = string + array[i]
    return string
```

