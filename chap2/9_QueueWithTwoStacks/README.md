# 面试题9：用两个栈实现队列

**题目：**用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )



LeetCode:[用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)



```python
class CQueue:

    def __init__(self, array=[]):
        self.dataArray = array                   # 数据栈
        self.helpArray = []                      # 辅助数据栈
        self.size = len(self.dataArray)          # 记录队列中元素

    def appendTail(self, value: int) -> None:   # 在队列尾部添加元素
        self.dataArray.append(value)
        self.size += 1
        return self.dataArray

    def deleteHead(self) -> int:                # 删除队列头部元素
        if self.size == 0:                      # 队列为空时
            return -1
        elif self.size >= 1:                    # 队列有元素时
            while len(self.dataArray) != 1:
                self.helpArray.append(self.dataArray.pop())
            param_2 = self.dataArray.pop()
            self.size -= 1

            self.dataArray = []                # 数据栈更新为空列表，然后再往原数据栈中添加元素
            while len(self.helpArray) > 0:
                self.dataArray.append(self.helpArray.pop())
            self.helpArray = []               # 辅助数据栈重新置为空列表
            return param_2

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()     
```

