# 面试题7：重建二叉树

**题目：**输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

```python
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```python
    3
   / \
  9  20
    /  \
   15   7
```



LeetCode:[重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)



```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # 前序遍历的顺序：中左右
        # 中序遍历的顺序：左中右

        length = len(preorder)
        if length == 0:
            return None

        # step1:构建头节点
        headValue = preorder.pop(0)  # 头节点的数值
        head = TreeNode(headValue)

        # step2：找到头节点在中序遍历数组的下标index
        # 在inorder数组中，0~index-1：为该头节点的左子树，index+1~末尾：为该头节点的右子树
        index = -1
        for index in range(len(inorder)):
            if inorder[index] == headValue:
                break
        head.left = self.buildTree(preorder[:index], inorder[:index])
        head.right = self.buildTree(preorder[index:], inorder[index + 1:])

        return head
```

