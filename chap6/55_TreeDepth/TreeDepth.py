# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#函数功能：采用递归方法求解二叉树的深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:                       # 输入节点为空时，返回节点的高度为0
            return 0
        leftHeight=self.maxDepth(root.left)  #当前节点左子树的高度
        rightHeight=self.maxDepth(root.right)#当前节点右子树的高度
        return max(leftHeight,rightHeight)+1