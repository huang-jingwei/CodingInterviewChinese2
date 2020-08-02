# 面试题35：复杂链表的复制

【题目】请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。





例如

![](image/e1.png)

```python
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

![](image/e3.png)

```python
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```



```python
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```

LeetCode:[复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/)



**解题思路**

采用哈希表进行存放节点信息，然后进行重构

```Python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None :             #输入节点是空节点,z直接返回空节点
            return None
      
        #将nodeData= {None:None}进行这样子的初始化，其实就是先将最后的空节点压入
        #否则在最后的重构链表节点时候，找不到空节点进行连接
        nodeData= {None:None}      #用字典结构存放节点信息 
        node=head   
        while node :
            nodeData[node]=Node(node.val)
            node=node.next
 
        node=head                  #连接节点，重构链表
        while node:
            nodeData[node].next=nodeData[node.next]
            nodeData[node].random=nodeData[node.random]
            node=node.next
        return nodeData[head]
```







