# 面试题22：链表中倒数第k个节点



【题目】输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

【例如】一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。



链表节点的定义

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```



LeetCode:[链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)



**解题思路** ：先计算该链表有多少个节点，这样便可以反推出所要求解的节点在链表中的顺序。

```Python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None:        # 判断输入的头结点是否为空
            return None
        nodeSum = 0             # 记录链表中节点的个数
        node = copy.copy(head)  # 复制头结点
        while node != None:
            nodeSum = nodeSum + 1
            node = node.next
        if k < 1 or k > nodeSum:  # 当k超过节点总个数或者k小于1（k默认从1开始）时，直接返回空
            return None
        count = 0                 # 从头开始遍历链表，记录当前节点为链表的第几个节点
        while count + k < nodeSum:
            head = head.next
            count = count + 1
        return head
```



