def reversePrint(head):
    stack = []
    while head != None:
        stack.append(head)
        head = head.next
    array = []
    while len(stack) > 0:
        array.append(stack.pop().val)
    return array