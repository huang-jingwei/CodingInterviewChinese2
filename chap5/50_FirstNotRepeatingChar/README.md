# 面试题50：第一个只出现一次的字符



【题目一】 字符串中第一个只出现一次的字符。

例如：在字符串中找到第一个出现一次的字符。例如输入"abaccdeff"。则输出'b'



牛客网OJ：[第一个只出现一次的字符](https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=11187&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)



**思路一：暴力解法**

最简单直接的方法就是对于每一个字符，循环判断后面的字符是不是跟它相同，直到查找到第一个只出现一次的那个字符即可

算法时间复杂度：O(N^2)

```Python
#函数功能：找到字符串中第一个只出现一次的字符
#基本思路：暴力搜索
# 对于每一个字符，循环判断后面的字符是不是跟它相同，直到查找到第一个只出现一次的那个字符即可
def FirstNotRepeatingChar_right(string):
    if string== None:                       # 判断输入是否为空
        return False
    for i in range(len(string)-1):          # 遍历字符串
        count=True                          # 布尔记录器，用来记录字符串中是否存在与改字符相同的字符
        for j in range(i+1,len(string)):
            if string[i]==string[j]:
                count=False                 #字符串中存在与改字符相同的字符
        if count==True:                     #若字符串中不存在与改字符相同的字符，直接返回
            return string[i]
    return False
```



**思路二：哈希表**

采用哈希表来记录字符串中每个字符出现的次数。

算法时间复杂度：O(N)

```python
#函数功能：照到字符串中第一个只出现一次的字符
#基本思路：采用哈希表来存放字符出现的次数
def UglyNumber(string):
    if string== None:            # 判断输入是否为空
        return False
    data={}                      # 初始化一个哈希表
    for i in string:             # 遍历字符串
        if i not in data:        #若哈希表中未出现过该元素，则字符对应的出现次数初始化为1
            data[i]=1
        else:
            data[i]=data[i]+1   # 反之，出现次数加一
    for i in string:            # 遍历字符串，在哈希表中搜索对应的字符出现的次数
        if data[i]==1:          # 若字符出现的次数为1，直接返回
            return i
    return False
```









