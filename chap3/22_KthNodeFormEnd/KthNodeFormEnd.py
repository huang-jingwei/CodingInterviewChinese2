import copy
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None:        # 判断输入的头结点是否为空
            return None
        nodeSum = 0             # 记录链表中节点的个数
        node = copy.copy(head)  # 复制头结点
        while node != None:
            nodeSum = nodeSum + 1
            node = node.next
        if k < 1 or k > nodeSum:  # 当k超过节点总个数或者k小于1（k默认从1开始）时，直接返回空
            return None
        count = 0                 # 从头开始遍历链表，记录当前节点为链表的第几个节点
        while count + k < nodeSum:
            head = head.next
            count = count + 1
        return head