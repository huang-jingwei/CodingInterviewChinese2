#函数功能：从上到下打印二叉树
#基本思路：二叉树的层次遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        data = []       # 队列结构
        nodeArray = []  # 层次遍历输出数组
        data.append(root)
        while len(data) > 0:
            node = data.pop(0)
            if node.left != None:
                data.append(node.left)
            if node.right != None:
                data.append(node.right)
            nodeArray.append(node.val)
        return nodeArray