# 面试题36：二叉搜索树与双向链表

【题目】输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

![](image/tree.png)



我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

![](image/list.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

LeetCode:[二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)



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







