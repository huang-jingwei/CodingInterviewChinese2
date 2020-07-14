# 面试题30：包含min函数的栈

【题目】定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



具体的函数结构如下

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def min(self) -> int:
```



LeetCode:[包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)



**解题思路**



1. 准备两个空栈，一个用来存放数据的数据栈，一个是用来记录栈中最小值的最小值栈
2. 在数据栈压入元素num的时候，元素num同时和最小值栈的栈顶元素min进行比较，如果最小值栈栈顶元素min≤num，那么在最小值栈中压入min，如果min≥num，那么就压入元素num
3. 这样最小值栈的栈顶元素就是数据栈的最小值。例子如下图所示



注意：在LeetCode中很奇葩的一点：在进行pop，top函数时，不需要对数据栈进行判空操作。下面所展示的代码是能通过LeetCode的。

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







