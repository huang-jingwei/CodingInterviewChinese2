class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        rows = len(grid)                                         # 获取礼物数组的行与列
        cols = len(grid[0])

        if rows == 1 and cols == 1:                              # 数组只有一个元素时，直接返回
            return grid[0][0]

        count = [[0 for i in range(cols)] for j in range(rows)]  # 初始化二维数组，记录不同位置能获得礼物的最大价值
        count[0][0] = grid[0][0]

        for rowIndex in range(rows):
            for colIndex in range(cols):
                # 起始点位置不做任何修改

                if rowIndex == 0 and colIndex > 0:    # 第一行元素
                    count[rowIndex][colIndex] = grid[rowIndex][colIndex] + count[rowIndex][colIndex - 1]
                elif colIndex == 0 and rowIndex > 0:  # 第一列元素
                    count[rowIndex][colIndex] = grid[rowIndex][colIndex] + count[rowIndex - 1][colIndex]
                elif rowIndex > 0 and colIndex > 0:   # 其他位置元素
                    count[rowIndex][colIndex] = grid[rowIndex][colIndex] + max(count[rowIndex - 1][colIndex],count[rowIndex][colIndex - 1])
        return count[rows - 1][cols - 1]

