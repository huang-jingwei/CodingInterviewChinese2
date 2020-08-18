# 面试题33：二叉搜索树的后序遍历序列

【题目】输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

```python
     5
    / \
   2   6
  / \
 1   3
```

例如:

```python
输入: [1,6,3,2,5]
输出: false

输入: [1,3,2,6,5]
输出: true
```

返回：[3,9,20,15,7]



LeetCode:[二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)



**解题思路：**

1、对二叉树的后序遍历的序列化结果进行反序列化，构造出原始二叉树；

2、对上一步所得到的二叉树进行层序遍历，判断是否符合搜索二叉树的要求。



```Python
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
```







