# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#函数功能：采用递归方法求解二叉树的深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:                       # 输入节点为空时，返回节点的高度为0
            return 0
        leftHeight=self.maxDepth(root.left)  #当前节点左子树的高度
        rightHeight=self.maxDepth(root.right)#当前节点右子树的高度
        return max(leftHeight,rightHeight)+1



#函数功能：采用层序遍历方法求解二叉树的深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:  #二叉树头结点为空时，树深度为0
            return 0
        depth=0        #初始化二叉树的深度
        queue=[]       #层次遍历的队列结构
        queue.append(root)

        while queue:
            temp=[]            #初始化列表，用来存放下一层节点
            for node in queue: #遍历当前层的节点，在temp结构中压入他们的儿子节点
                if node.left !=None:
                    temp.append(node.left)
                if node.right !=None:
                    temp.append(node.right)
            queue=temp
            depth +=1
        return depth