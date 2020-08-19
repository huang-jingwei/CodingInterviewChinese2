# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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