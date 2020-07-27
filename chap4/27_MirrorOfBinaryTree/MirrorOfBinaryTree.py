# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        item=root.left
        root.left=self.mirrorTree(root.right)
        root.right=self.mirrorTree(item)
        return root     