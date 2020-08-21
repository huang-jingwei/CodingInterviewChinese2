# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        # 搜索二叉树的中序遍历就是单调递增序列
        array = self.inOrder(root)

        # 断掉节点之间的连接进行重新连接
        for index in range(len(array) - 1):         # 重新连接右节点
            array[index].right = array[index + 1]
        for index in range(len(array) - 1, 0, -1):  # 重新连接左节点
            array[index].left = array[index - 1]
        array[-1].right = array[0]                  # 连接头尾两节点
        array[0].left = array[-1]
        return array[0]

    # 二叉树的中序遍历序列化
    def inOrder(self, root):
        array = []
        if root == None:
            return []
        left = self.inOrder(root.left)
        if len(left) > 0:
            for item in left:
                array.append(item)
        array.append(root)
        right = self.inOrder(root.right)
        if len(right) > 0:
            for item in right:
                array.append(item)
        return array