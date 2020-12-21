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
