# 面试题54:二叉搜索树的第k大节点



【题目】 给定一棵二叉搜索树，请找出其中第k大的节点。



```python
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
```



LeetCode:[二叉搜索树的第k大节点](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)



二叉树数节点定义

```Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```



**解题思路：**

二叉搜索树的中序遍历就是单调递增序列

```python
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 搜索二叉树的中序遍历是单调递增序列
        array = self.inOrder(root)
        return array[-k]

    # 二叉树中序遍历的序列化形式
    def inOrder(self, root):
        array = []
        if root == None:
            return []

        leftNode = self.inOrder(root.left)
        if len(leftNode) > 0:
            for nodeVal in leftNode:
                array.append(nodeVal)

        array.append(root.val)

        rightNode = self.inOrder(root.right)
        if len(rightNode) > 0:
            for nodeVal in rightNode:
                array.append(nodeVal)
        return array
```



