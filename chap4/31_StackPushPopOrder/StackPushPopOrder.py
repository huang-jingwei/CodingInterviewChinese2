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