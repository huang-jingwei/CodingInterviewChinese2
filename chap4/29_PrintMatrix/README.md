# 面试题29：顺时针打印矩阵

【题目】定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



【例如】

```python
输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```



```
输入：matrix = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```



LeetCode:[顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)



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







