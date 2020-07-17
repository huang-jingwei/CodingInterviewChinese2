# 面试题23：链表中环的入口节点



【题目】给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

【例如】

```python
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
```

![](image/circularlinkedlist.png)



```python
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
```

![](image/circularlinkedlist_test3.png)



链表节点的定义

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```



LeetCode:[环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)



**解题思路：**

在对原链表进行顺序遍历时，储存当前节点的节点信息，若链表中存在回环，那么出现过的节点还会再次出现。那么第一次出现重复节点的时候，就是链表中环的入口。



```Python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:              # 如果输入的头结点为空，直接返回None
            return None
        nodeData = {}                 # 初始化一个空字典，用来记录节点信息
        while head != None:
            if head not in nodeData:  # 记录当前节点信息
                nodeData[head] = 1
            # 若当前节点的下一节点已经在字典中出现过，证明这就是列表入环的入口
            if (head.next != None) and (head.next in nodeData):
                return head.next
            # 节点下移动一位
            head = head.next
        return None
```



