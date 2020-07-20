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