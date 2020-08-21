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
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        # 搜索二叉树的中序遍历就是单调递增序列
        array = self.inOrder(root)

        # 断掉节点之间的连接进行重新连接
        for index in range(len(array) - 1):         # 重新连接右节点
            array[index].right = array[index + 1]
        for index in range(len(array) - 1, 0, -1):  # 重新连接左节点
            array[index].left = array[index - 1]
        array[-1].right = array[0]                  # 连接头尾两节点
        array[0].left = array[-1]
        return array[0]

    # 二叉树的中序遍历序列化
    def inOrder(self, root):
        array = []
        if root == None:
            return []
        left = self.inOrder(root.left)
        if len(left) > 0:
            for item in left:
                array.append(item)
        array.append(root)
        right = self.inOrder(root.right)
        if len(right) > 0:
            for item in right:
                array.append(item)
        return array
```







