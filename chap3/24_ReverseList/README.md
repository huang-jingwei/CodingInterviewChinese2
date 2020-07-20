# 面试题24：反转链表



【题目】定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

例如：

```python
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```



链表节点的定义

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```



LeetCode:[反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)



解题思路：储存当前节点的上一节点，在对原链表进行顺序遍历时，同时对节点进行反向连接。



```Python
import copy
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:        # 判断输入的头结点是否为空
            return head
        elif head.next == None:  # 链表只有一个节点
            return head
        curNode = head          # 当前节点节点
        preNode = None          # 当前节点的上一节点
        while curNode != None:
            nexyNode = copy.copy(curNode.next)  # 获得当前节点的下一节点
            curNode.next = preNode              # 链表节点反向连接
            
            preNode = curNode                   # 节点右移动，更新节点
            curNode = nexyNode
        return preNode
```



