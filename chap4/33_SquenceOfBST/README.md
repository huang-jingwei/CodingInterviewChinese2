# 面试题33：二叉搜索树的后序遍历序列

【题目】输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

```python
     5
    / \
   2   6
  / \
 1   3
```

例如:

```python
输入: [1,6,3,2,5]
输出: false

输入: [1,3,2,6,5]
输出: true
```

返回：[3,9,20,15,7]



LeetCode:[二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)



**解题思路：**

1、在解题前先复习基本知识点

- 后序遍历的顺序是：左右中
- 二叉搜索树定义：左子树中所有节点的值 << 根节点的值；右子树中所有节点的值 >> 根节点的值；其左、右子树也分别为二叉搜索树。

2、采用递归的方法，将后序遍历结果分为两段，分别来验证准确性

```Python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verifyPostorder(self, postorder):
        treeLength = len(postorder)
        if treeLength == 0 or treeLength == 1:     # 二叉树没有节点或只有一个节点时，为搜索二叉树
            return True
        return self.reConstruction(postorder,left=0,right=len(postorder)-1)


    #根据后序遍历结果判断二叉树是否是搜索二叉树
    def reConstruction(self,postorder,left,right):
        if left >=right:
            return  True
        #因为后序遍历的顺序为：左右中
        #所以后序遍历的尾节点是头结点
        headVal=postorder[right]

        mid = left-1
        #搜索二叉树节点数值比左儿子节点数值大，比右儿子节点数值小
        #找到当前节点的左子树和右子树的分界点
        while mid+1<=right and postorder[mid+1] < headVal:
            mid  += 1
        #若该二叉树为搜索二叉树，那么分界点的数值(除去最后元素）均大于头结点
        rightIndex=mid
        while rightIndex+1<len(postorder) and postorder[rightIndex+1]>postorder[right]:
            rightIndex +=1
        return  rightIndex==right-1 and self.reConstruction(postorder,mid+1,right-1) and self.reConstruction(postorder,left,mid)
```







