# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        # 二叉树的先序遍历序列化，中左右
        string1 = self.preTreeNode(root).split("!")
        # 二叉树的先序遍历序列化进行修改，中右左
        string2 = self.preTreeNode2(root).split("!")

        if string1 == string2:
            return True
        else:
            return False

    # 二叉树的先序遍历序列化,顺序：中左右
    def preTreeNode(self, node):
        if node == None:
            return "#!"
        string = ""
        string = string + str(node.val) + "!"
        string = string + str(self.preTreeNode(node.left))
        string = string + str(self.preTreeNode(node.right))
        return string

    # 对二叉树的先序遍历序列化进行修改,顺序：中右左
    def preTreeNode2(self, node):
        if node == None:
            return "#!"
        string = ""
        string = string + str(node.val) + "!"
        string = string + str(self.preTreeNode2(node.right))
        string = string + str(self.preTreeNode2(node.left))
        return string
