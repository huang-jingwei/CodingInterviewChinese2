# 面试题55：二叉树的深度

【题目】输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

```python
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。





LeetCode:[二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)



**思路一：递归方法**

一颗树的高度就是它左子树高度和右子树高度的较大者，然后再加1。

```Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:                       # 输入节点为空时，返回节点的高度为0
            return 0
        leftHeight=self.maxDepth(root.left)  #当前节点左子树的高度
        rightHeight=self.maxDepth(root.right)#当前节点右子树的高度
        return max(leftHeight,rightHeight)+1
```



**思路二：层序遍历**

**关键点：** 每遍历一层，则计数器 +1+1 ，直到遍历完成，则可得到树的深度。

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
```


