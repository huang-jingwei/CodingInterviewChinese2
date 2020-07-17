class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:              # 如果输入的头结点为空，直接返回None
            return None
        nodeData = {}                 # 初始化一个空字典，用来记录节点信息
        while head != None:
            if head not in nodeData:  # 记录当前节点信息
                nodeData[head] = 1
            # 若当前节点的下一节点已经在字典中出现过，证明这就是列表入环的入口
            if (head.next != None) and (head.next in nodeData):
                return head.next
            # 节点下移动一位
            head = head.next
        return None