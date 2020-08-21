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
        if len(preorder) == 0:
            return None
        head = self.reconstruction(preorder, inorder, 0, 0, len(inorder) - 1)

        return head

    def reconstruction(self, preorder, inorder, headIndex, left, right):
        if left > right:
            return None
        headVal = preorder[headIndex]
        head = TreeNode(headVal)         # 建立当前子树的根节点
       
        # 中序遍历的顺序是：左中右
        # 找出在中序遍历中，左右子树的分界点
        mid = left
        for index in range(len(inorder)):
            if inorder[index] == headVal:
                mid = index
        head.left = self.reconstruction(preorder, inorder, headIndex + 1, left, mid - 1)
        head.right = self.reconstruction(preorder, inorder, mid - left + headIndex + 1, mid + 1, right)
        return head  
```

