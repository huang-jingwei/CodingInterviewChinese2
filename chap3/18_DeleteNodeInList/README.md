# 面试题18：删除链表的节点

【题目一】在O(1)时间内删除链表节点。

给定单向链表的头指针和一个要删除的节点的值，定义一个函数在O(1)时间内删除该节点。返回删除后的链表的头节点。



例如：

```python
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

```python
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```




《剑指offer》书上的原题和LeetCode的题目有所区别。

1、原题分别给出头节点和被删除的节点对应的指针，这样能O(1)时间内删除链表节点。

2、而LeetCode上是只能给出头节点的指针，这样只能O(N)时间内删除链表节点实现。



为了能在OJ上进行代码测试，题目以LeetCode为准。链表节点与函数的定义如下

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
```



LeetCode:[删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)



**思路一：暴力解法**

采用遍历的方式从链表的头结点开始，顺序遍历查找要删除的节点，并在链表中删除该节点

算法时间复杂度：O(N)

```Python
# 函数功能：调整数组顺序使奇数位于偶数前面
# 基本思路：借鉴荷兰国旗问题的解法
def ReorderArray(array):
    if array==None or len(array)==0:    # 输入为空数组时，直接输出
        return array
    more=len(array)                     # 数组中，下标≥more的位置均为偶数
    index = 0                           # 初始化移动下标
    while index<more:
        if array[index]%2==1:           # 该位置元素为奇数时，移动下标右前进一位
            index=index+1
        else:                           # 该位置元素为偶数时，more减一，当前位置与more位置交换元素
            more=more-1                 # 注意此时index不可右前进一位，因为并不知道新交换过来的数值的奇偶性
            array[index],array[more]=array[more],array[index]
    return array
```



