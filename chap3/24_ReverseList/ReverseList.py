import copy
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:        # 判断输入的头结点是否为空
            return head
        elif head.next == None:  # 链表只有一个节点
            return head
        curNode = head          # 当前节点节点
        preNode = None          # 当前节点的上一节点
        while curNode != None:
            nexyNode = copy.copy(curNode.next)  # 获得当前节点的下一节点
            curNode.next = preNode              # 链表节点反向连接

            preNode = curNode                   # 节点右移动，更新节点
            curNode = nexyNode
        return preNode