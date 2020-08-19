# 面试题6：从尾到头打印链表

**【题目】：**  输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

链表节点结构的定义

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```





LeetCode:[从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)





【解题思路】

逆序打印实质上就是数据的先进后出。那么这道题目可以结合栈结构进行求解。

1、遍历链表，依次将节点压入数据栈；

2、遍历结束后，再依次从数据栈中弹出元素，这样就可以实现链表元素的逆序打印。

```python
def reversePrint(head):
    stack = []
    while head != None:
        stack.append(head)
        head = head.next
    array = []
    while len(stack) > 0:
        array.append(stack.pop().val)
    return array
```

