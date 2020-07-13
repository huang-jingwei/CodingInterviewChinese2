# 面试题51：数组中的逆序对



【题目】 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。 输入一个数组，求出这个数组中的逆序对的总数

例如：在数组{7,5,6,4}中，一共存在五个逆序对，分别是（7,6）、(7,5)、（7,4）、（6,4）和(5,4)



牛客网OJ：[数组中的逆序对](https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)



**思路一：暴力解法**

最简单直接的方法就是每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对。

算法时间复杂度：O(N^2)

```Python
# 函数功能：找到数组中的逆序对个数
# 基本思路：暴力搜索
# 每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对
# 算法时间复杂度：O(N^2)
def InversePairs_right(array):
    if array== None or len(array)==0:       # 判断输入是否为空
        return 0
    count = 0                               # 初始化计数器，用来记录逆序对的总个数
    for i in range(len(array)):             # 遍历数组
        for j in range(i+1,len(array)):
            if array[i]>array[j]:           # 找到逆序对，计数器加一
                count=count+1              
    return count
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









