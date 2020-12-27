# 面试题12：矩阵中的路径



【题目】请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。



【例如】在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a"," **b** ","c","e"],

["s"," **f** ","c","s"],

["a","d"," **e** ","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



**示例 1：**

```python
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```





LeetCode:[矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

采用岛问题+回溯法解决该问题

1、岛问题的具体思路参考第13题；

2、这里的回溯法取消占用的思路要了解。

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordArray = list(word)  # 将字符串转化为字符列表

        self.row = len(board)  # 矩阵的行、列
        self.col = len(board[0])
        self.board = board  # 将矩阵映射到成全局变量
        # 记录走过的路径
        view = [[False for i in range(self.col)] for j in range(self.row)]

        for rowIndex in range(self.row):
            for colIndex in range(self.col):
                result = self.infect(view, rowIndex, colIndex, 0, wordArray)
                if result == True:
                    return True
        return False

    def infect(self, array, rowIndex, colIndex, index, wordArray):
        # 字符串数组已经被遍历结束，则视作搜索成功
        if index >= len(wordArray):
            return True
        # 防止下标越界
        if rowIndex < 0 or rowIndex >= self.row or colIndex < 0 or colIndex >= self.col:
            return False
        # 矩阵当前位置未能与字符串对应位置进行匹配
        elif self.board[rowIndex][colIndex] != wordArray[index]:
            return False
        # 矩阵当前下标已被占用
        elif array[rowIndex][colIndex] == True:
            return False

        array[rowIndex][colIndex] = True  # 占用该位置
        index += 1

        # 沿着四个方向进行搜索，只要有一个方向成功，便视作成功
        result = self.infect(array, rowIndex + 1, colIndex, index, wordArray) or \
                 self.infect(array, rowIndex - 1, colIndex, index, wordArray) or \
                 self.infect(array, rowIndex, colIndex + 1, index, wordArray) or \
                 self.infect(array, rowIndex, colIndex - 1, index, wordArray)

        # 搜索成功便返回，反之取消占用
        if result == True:
            return True
        array[rowIndex][colIndex] = False
        return False
```
























