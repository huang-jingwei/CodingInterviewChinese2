# 面试题52：两个链表的第一个公共节点



【题目】 输入两个链表，找出它们的第一个公共节点。



链表节点的定义如下

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

【例如】

如下面的两个链表：在节点 c1 开始相交。

![](images/160_statement.png)





```python
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
```

![](images/160_example_1.png)



LeetCode:[两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)



**解题思路**

1、计算出两个链表的长度lengthNodeA和lengthNodeB，从而得到两个链表的长度差lengthGap；

2、长度较长的列表对应的头结点先移动，移动长度为lengthGap；

3、经过上面的调整步骤后，此时两个链表的节点距离公共节点的距离是一样的。那么此时让两个节点同时移动就能找出公共节点。



算法时间复杂度：O(N)

```Python
import copy
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:      # 判断输入节点是否为空
            return None
        # 分别计算两个链表的长度,从而计算出两个链表的长度差
        nodeA = copy.copy(headA)
        nodeB = copy.copy(headB)
        lengthNodeA = 0
        lengthNodeB = 0
        while nodeA != None:
            lengthNodeA = lengthNodeA + 1
            nodeA = nodeA.next
        while nodeB != None:
            lengthNodeB = lengthNodeB + 1
            nodeB = nodeB.next
        lengthGap = abs(lengthNodeA - lengthNodeB)  # 两个链表长度差

        # 长度较长的列表的头结点先进行移动，移动距离是两个链表的长度差
        if lengthNodeA >= lengthNodeB:
            while lengthGap > 0:
                lengthGap = lengthGap - 1
                headA = headA.next
        else:
            while lengthGap > 0:
                lengthGap = lengthGap - 1
                headB = headB.next

        # 通过上面的调整，此时两个链表的节点距离公共交点的距离是一致的
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
```











