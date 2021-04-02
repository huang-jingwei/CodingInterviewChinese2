# 面试题 28： 对称的二叉树

【题目】请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

【例如】 二叉树 [1,2,2,3,4,4,3] 是对称的。 

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```



```python
输入：root = [1,2,2,3,4,4,3]
输出：true

输入：root = [1,2,2,null,3,null,3]
输出：false
```



LeetCode: [对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)



**解题思路**  ：二叉树序列化

1、先采用先序遍历的方式，节点遍历顺序为：中左右，对二叉树进行序列化。

2、对先序遍历方法进行修改，节点遍历顺序为：中右左，然后对二叉树进行序列化。

若二叉树是对称二叉树，那么这两种方法序列化所得到结果应该是一致的。



```Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        
        #二叉树的先序遍历序列化，中左右
        string1=self.preTreeNode(root).split("!")
        #二叉树的先序遍历序列化进行修改，中右左
        string2=self.preTreeNode2(root).split("!")

        if string1==string2:
            return True
        else:
            return False
    

    #二叉树的先序遍历序列化,顺序：中左右
    def preTreeNode(self,node):
        if node==None:
            return "#!"
        string=""
        string=string+str(node.val)+"!"
        string=string+str(self.preTreeNode(node.left))
        string=string+str(self.preTreeNode(node.right))
        return string
    
    #对二叉树的先序遍历序列化进行修改,顺序：中右左
    def preTreeNode2(self,node):
        if node==None:
            return "#!"
        string=""
        string=string+str(node.val)+"!"
        string=string+str(self.preTreeNode2(node.right))
        string=string+str(self.preTreeNode2(node.left))
        return string
      
```





**解题思路二**  ：层次遍历

1、采用层次遍历对二叉树进行遍历。

2、对称二叉树的每一层节点的二叉树都是对称的。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        
        queue=[root]
        while len(queue)>0:
            # step1:判断当前层节点是否对称
            left=0
            right=len(queue)-1
            while left<right:
                if queue[left]==None:
                    if queue[right]!=None: return False
                elif queue[right]==None:
                    if queue[left]!=None: return False
                elif queue[left].val !=queue[right].val:
                    return False
                left +=1
                right-=1

            # step2:储存下一层节点
            isLeaf=True   # 布尔器，判断当前层是否是二叉树最底层
            nextNode=[]
            for node in queue:
                if node==None:
                    nextNode.append(None)
                    nextNode.append(None)
                else:
                    nextNode.append(node.left)
                    nextNode.append(node.right)
                    if node.left!=None or node.right !=None:
                        isLeaf=False
            
            if isLeaf==True:
                break
            else:
                queue=nextNode
        return True
```





