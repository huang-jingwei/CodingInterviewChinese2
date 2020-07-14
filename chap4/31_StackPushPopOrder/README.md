# 面试题31：栈的压入、弹出序列

【题目】输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。



例如

```python
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```



LeetCode:[栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)



**解题思路**

开辟一个辅助栈stack，模拟入栈出战过程(假设pushed为入栈序列，poped为出栈序列)

- pushed中的元素依次压入辅助栈stack
- 新压入的元素与弹出序列的栈底相同，辅助栈弹出，同时poped向右移动
- 不相同了pushed中的元素继续入辅助栈stack

```Python
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
```







