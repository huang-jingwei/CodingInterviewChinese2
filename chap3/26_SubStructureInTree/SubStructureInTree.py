# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None:  # 空树不是任何树的子树
            return False
        # 如果直接给的 A B 两棵树满足条件，直接返回True
        if self.isSubtree(A, B) == True:
            return True
        # 否则分别在A的左右子树寻找是否含有B
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSubtree(self, A: TreeNode, B: TreeNode) -> bool:
        # b都遍历完了，还没发现不一样的，说明那就一样了
        if B == None:
            return True
        # 压根就没有a，当然不行
        if A == None:
            return False
        # 节点数值不一样，那就不能算是同一棵树
        if A.val != B.val:
            return False
        return self.isSubtree(A.left, B.left) and self.isSubtree(A.right, B.right)       