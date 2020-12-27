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