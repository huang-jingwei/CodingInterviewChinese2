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



```Python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array=[]       #初始化数据栈，用来存放数据
        self.minArray=[]    #初始化最小数据栈，栈顶数据即为数据栈最小的元素


    def push(self, x: int) -> None:
        self.array.append(x)               #数据栈直接压入元素
        if len(self.minArray)==0:
            self.minArray.append(x)
        else:
            if x<=self.minArray[-1]:
                self.minArray.append(x)
            else:
                self.minArray.append(self.minArray[-1])


    def pop(self) -> None:
        item=self.array.pop()
        self.minArray.pop()
        return item


    def top(self) -> int:
        return self.array[-1]


    def min(self) -> int:
        return self.minArray[-1]
```







