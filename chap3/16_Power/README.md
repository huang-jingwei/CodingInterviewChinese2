# 面试题51：数组中的逆序对



【题目】 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。 输入一个数组，求出这个数组中的逆序对的总数

例如：在数组{7,5,6,4}中，一共存在五个逆序对，分别是（7,6）、(7,5)、（7,4）、（6,4）和(5,4)



LeetCode:[数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)



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











