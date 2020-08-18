# 面试题26：树的子结构



【题目】输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

**例如:**
给定的树 A:



```python
     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
```



返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

**示例 ：**

```Python
输入：A = [1,2,3], B = [3,1]
输出：false

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
```



LeetCode:[树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)





**解题思路**



```Python
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
```



