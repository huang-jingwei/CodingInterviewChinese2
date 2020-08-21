# 面试题34：二叉树中和为某一值的路径

【题目】输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。





例如
给定如下二叉树，以及目标和 `sum = 22`，



```python
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```

返回:

```python
[
   [5,4,11,2],
   [5,8,4,5]
]
```



LeetCode:[二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)



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







