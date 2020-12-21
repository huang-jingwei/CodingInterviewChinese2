# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        inorderArray = self.inorderPrint(root)  # 中续遍历数组
        length = len(inorderArray)  # 二叉树节点个数

        for index in range(length):
            if inorderArray[index] == p:
                break
        if index < length - 1:
            return inorderArray[index + 1]
        else:
            return None

    # 函数功能：实现二叉树的中续遍历
    def inorderPrint(self, root):
        array = []
        if root == None:
            return []

        leftArray = self.inorderPrint(root.left)
        if len(leftArray) > 0:
            for node in leftArray:
                array.append(node)

        array.append(root)

        rightArray = self.inorderPrint(root.right)
        if len(rightArray) > 0:
            for node in rightArray:
                array.append(node)

        return array