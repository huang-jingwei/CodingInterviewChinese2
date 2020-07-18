# 面试题52：两个链表的第一个公共节点



【题目】 输入两个链表，找出它们的第一个公共节点。

【例如】

如下面的两个链表：在节点 c1 开始相交。

![](images/160_statement.png)





```python
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

![](images/160_example_1.png)



LeetCode:[两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)



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











