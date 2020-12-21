# 面试题8：二叉树的下一节点

**题目：**设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回`null`。



**示例 1:**

```python
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
```

**示例 2:**

```python
输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null


```



LeetCode:[后继者](https://leetcode-cn.com/problems/successor-lcci/)

解题思路：暴力解法

直接输出二叉树的后续遍历数组，再找出该节点的后继节点

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        
        inorderArray=self.inorderPrint(root) # 中续遍历数组
        length=len(inorderArray)             # 二叉树节点个数

        for index in range(length):
            if inorderArray[index]==p:
                break
        if index<length-1:
            return inorderArray[index+1]
        else:
            return None

    # 函数功能：实现二叉树的中续遍历
    def inorderPrint(self,root):
        array=[]
        if root==None:
            return []
        
        leftArray=self.inorderPrint(root.left)
        if len(leftArray)>0:
            for node in leftArray:
                array.append(node)

        array.append(root)

        rightArray=self.inorderPrint(root.right)
        if len(rightArray)>0:
            for node in rightArray:
                array.append(node)

        return array
```

