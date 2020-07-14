
#函数功能：判断整数序列poped是否为整数序列pushed的弹出序列
#参数说明：pushed，popped分别为两个整数序列

def StackPushPopOrder(pushed,popped):
    stack = []  # 辅助数据栈，用来模拟数据进栈和出栈过程
    index = 0   # 移动下标，用来记录弹出元素在弹出数据栈的下标
    for num in pushed:     # 遍历输入数据栈
        stack.append(num)  # 数据入账

        # 如果数据栈的栈顶元素和弹出数据栈的头部元素相同，即数据栈中该元素此时应该弹出
        while len(stack) != 0 and stack[-1] == popped[index]:
            stack.pop()
            index = index + 1
    # 若弹出数据栈为输入数据栈的弹出序列，那么此时应该弹出数据栈应该已经遍历结束了
    # 移动光标提取走一步，所以此时index应该为len(poped)
    return index == len(popped)