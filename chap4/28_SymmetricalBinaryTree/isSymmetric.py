# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        queue = [root]
        while len(queue) > 0:
            # step1:判断当前层节点是否对称
            left = 0
            right = len(queue) - 1
            while left < right:
                if queue[left] == None:
                    if queue[right] != None: return False
                elif queue[right] == None:
                    if queue[left] != None: return False
                elif queue[left].val != queue[right].val:
                    return False
                left += 1
                right -= 1

            # step2:储存下一层节点
            isLeaf = True  # 布尔器，判断当前层是否是二叉树最底层
            nextNode = []
            for node in queue:
                if node == None:
                    nextNode.append(None)
                    nextNode.append(None)
                else:
                    nextNode.append(node.left)
                    nextNode.append(node.right)
                    if node.left != None or node.right != None:
                        isLeaf = False

            if isLeaf == True:
                break
            else:
                queue = nextNode
        return True