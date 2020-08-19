# 面试题7：重建二叉树

**题目：**输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

```python
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```python
    3
   / \
  9  20
    /  \
   15   7
```



LeetCode:[重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)



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

