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



采用遍历的方式从链表的头结点开始，顺序遍历查找要删除的节点，并在链表中删除该节点

算法时间复杂度：O(N)

```Python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        # 要删除的节点是头结点
        if head.val == val:
            nextNode = head.next  # 直接用下一节点覆盖头结点
            head = nextNode
            return head

        # 要删除的节点是除头结点外的其他节点
        preNode = head           # 当前节点的下一节点
        node = head.next         # 当前节点 

        # 要删除的节点是中间节点
        while node != None:
            if node.val == val and node.next == None:  # 要删除的节点是尾节点
                preNode.next = None                    # 上一节点的相邻节点直接指向空
                return head

            if node.val == val and node.next != None:  # 要删除的节点是位于链表中间的节点
                nextNode = node.next
                preNode.next = nextNode
                return head
            
            preNode = node                             # 当前节点不是要删除的节点，节点向下移动
            node = node.next 
```



