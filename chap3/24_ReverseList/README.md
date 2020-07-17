# 面试题24：反转链表



【题目】定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

例如：

```python
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```



链表节点的定义

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```



LeetCode:[反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)



解题思路：用一个数组来存放链表顺序遍历的节点信息，然后在反向遍历数组来重新连接链表节点。



```Python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None:       #判断输入是否为空
            return None
        array=[]                        #初始化数组来存放节点的信息  
        while l1 !=None and l2 !=None:  #遍历两个链表，采用类似外排的方法对链表的节点进行排序
            if l1.val<=l2.val:
                array.append(l1)
                l1=l1.next
            else:
                array.append(l2)
                l2=l2.next
        
        #至少有一个列表被遍历完了
        #把剩下的节点信息放入数组array中
        if l1 ==None:
            while l2 !=None:
                array.append(l2)
                l2=l2.next
        else:
            while l1 !=None:
                array.append(l1)
                l1=l1.next
        
        #把数组array的节点进行重新连接
        for index in range(len(array)-1):
            array[index].next=array[index+1]
        return array[0]
```



