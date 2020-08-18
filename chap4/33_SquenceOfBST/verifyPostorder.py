# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verifyPostorder(self, postorder):
        treeLength = len(postorder)
        if treeLength == 0 or treeLength == 1:
            return True
        head = self.rePostorder(postorder)  # 二叉树的后续遍历反序列化
        print(treePostPrint(head))
        nodeData = self.LevelOrder(head)  # 二叉树的层序遍历序列化
        # 根据二叉树的层序遍历的序列化结果
        # 判断该二叉树是否是搜索二叉树
        for index in range(len(nodeData)):
            if nodeData[index] != None:
                leftIndex = 2 * index + 1
                rightIndex = 2 * index + 2

                if leftIndex < len(nodeData) and nodeData[leftIndex] != None and nodeData[index] < nodeData[leftIndex]:
                    return False
                if rightIndex < len(nodeData) and nodeData[rightIndex] != None and nodeData[index] > nodeData[
                    rightIndex]:
                    return False
        return True

    # 后序遍历的反序列化
    def rePostorder(self, postorder):
        if len(postorder) <= 0:
            return None
        val=postorder.pop()
        root=None
        if val != '#':
            root = TreeNode(val)
            root.right = self.rePostorder(postorder)
            root.left = self.rePostorder(postorder)
        return root

    # 二叉树的层序遍历的序列化
    def LevelOrder(self, head):
        queue = []  # 层序遍历的辅助队列
        stack = []  # 层序遍历得到的二叉树节点
        queue.append(head)
        while len(queue) > 0:
            node = queue.pop(0)

            if node != None:
                stack.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                stack.append(None)
        # 去除叶节点的左右儿子节点
        while len(stack) > 0 and stack[-1] == None:
            stack.pop()
        print(stack)
        return stack

def treePostPrint(root):
    array=""
    if root==None:
        array=array+"#!"
    else:
        array=array+treePostPrint(root.left)
        array=array+treePostPrint(root.right)
        array=array+str(root.val)+"!"
    return array


postorder=[4, 8, 6, 12, 16, 14, 10]
postorder=[1,6,3,2,5]
test=Solution()
print(test.verifyPostorder(postorder))