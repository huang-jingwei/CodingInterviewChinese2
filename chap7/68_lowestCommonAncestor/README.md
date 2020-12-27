# 面试题68 . 二叉搜索树的最近公共祖先

【题目一】给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

![](image/binarysearchtree_improved.png)

**示例 1:**

```python
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

```

**示例 2:**

```python
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```



LeetCode:[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)



**题目分析**

本题给定了两个重要条件：① 树为 二叉搜索树 ，② 树的所有节点的值都是 唯一 的。根据以上条件，可方便地判断 p,q与 root 的子树关系，即：

- 若 root.val < p.val，则 p在 root  右子树 中；
- 若 root.val > p.val，则 p在 root 左子树 中；
- 若 root.val = p.val，则 p和root  指向 同一节点 。



基本思路：循环搜索

当节点 root 为空时跳出；

- 当 p, q都在root 的 右子树 中，则遍历至 root.right；
- 否则，当 p, q都在 root  的 左子树 中，则遍历至 root.left；
- 否则，说明找到了 最近公共祖先 ，跳出。

返回值： 最近公共祖先 root。



```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        
        if root.val< p.val and root.val <q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        return root
```





【题目二】给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

![](image/binarytree.png)

**示例 1:**

```python
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```

**示例 2:**

```python
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
```



LeetCode:[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)



**题目分析**

最近公共祖先的定义： 设节点 root为节点 p, q的某公共祖先，若其左子节点 root.left 和右子节点 root.right 都不是 p,q的公共祖先，则称 root是 “最近的公共祖先” 。

根据以上定义，若 root 是 p, q的 最近公共祖先 ，则只可能为以下情况之一：

- p和 q 在 root的子树中，且分列 root的 异侧（即分别在左、右子树中）；
- p = root，且 q 在 root 的左或右子树中；
- q = root，且 p在 root的左或右子树中；



考虑通过递归对二叉树进行后序遍历，当遇到节点 p或 q时返回。从底至顶回溯，当节点 p, q在节点 root的异侧时，节点 root即为最近公共祖先，则向上返回 root。

**递归解析：**
**终止条件：**

1. 当越过叶节点，则直接返回 null ；
2. 当 root等于 p, q ，则直接返回 root；

**递推工作：**

1. 开启递归左子节点，返回值记为 left；
2. 开启递归右子节点，返回值记为 right ；

**返回值：**  根据 left和 right，可展开为四种情况；

1. 当 left和 right同时为空 ：说明 root的左 / 右子树中都不包含 p,q，返回 null；

2. 当 left和 right同时不为空 ：说明 p, q 分列在 root的 异侧 （分别在 左 / 右子树），因此 root为最近公共祖先，返回 root ；

3. 当 left为空 ，right不为空 ：p,q都不在 root的左子树中，直接返回 right。具体可分为两种情况：

   

   p,q其中一个在 root的 右子树 中，此时 right指向 p（假设为 p）；

   

   p,q两节点都在 root的 右子树 中，此时的 right指向 最近公共祖先节点 ；
   当 left不为空 ， right为空 ：与情况 3. 同理；





```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root==None:
            return None
       
        #递归查询两个节点p q，如果某个节点等于节点p或节点q，则返回该节点的值给父节点
        if root==p or root==q:
            return root  

        # 判断当前节点的左右字树是否存在p，q节点
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)


        # 如果当前节点的左右子树分别包括p和q节点，那么这个节点必然是所求的解
        if left !=None and right !=None:
            return root
        
        #如果当前节点有一个子树的返回值为p或q节点，则返回该值。（告诉父节点有一个节点存在其子树中）
        if left !=None :
            return left
        if  right!=None:
            return right
        return None
```

