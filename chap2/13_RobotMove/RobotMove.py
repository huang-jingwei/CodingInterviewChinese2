class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if m <= 0 or n <= 0 or k < 0:  # 输入为非正数时，为非法输入
            return 0
        rows = m  # 矩阵的行列数
        cols = n
        visted = [False] * (rows * cols)  # 布尔列表，记录该位置是否被访问过,False为未访问过，反之为True
        count = self.movingCountCore(k, rows, cols, 0, 0, visted)  # 记录机器人能运动的方格数量
        return count

    def movingCountCore(self, k, rows, cols, currentRow, currentCol, visted):
        count = 0  # 记录机器人从该位置开始搜索，能找到的符合要求的方格数量
        if self.checkPosition(k, rows, cols, currentRow, currentCol, visted):  # 判断该位置是否符合运动规则
            visted[currentRow * cols + currentCol] = True  # 列表中相邻的col个为一行位置的访问布尔数值
            # 沿着四个方向继续搜索
            count = 1 + self.movingCountCore(k, rows, cols, currentRow - 1, currentCol, visted) \
                    + self.movingCountCore(k, rows, cols, currentRow + 1, currentCol, visted) \
                    + self.movingCountCore(k, rows, cols, currentRow, currentCol - 1, visted) \
                    + self.movingCountCore(k, rows, cols, currentRow, currentCol + 1, visted)
        return count

    # 判断该坐标位置是否符合机器人的运动规则，主要包含两个规则
    # 规则一：坐标不越过矩阵范围
    # 规则二：坐标列表行坐标和列坐标的数位之和要≤数字k
    # 输出参数说明：True：该下标合法，False：该下标不合法
    def checkPosition(self, k, rows, cols, currentRow, currentCol, visted):
        if currentRow >= rows or currentCol >= cols or currentRow < 0 or currentCol < 0:  # 判断当前下标是否符合规则
            return False
        if visted[currentRow * cols + currentCol] == True:  # 判断当前位置是否已经被访问过
            return False
        if self.numDigitSum(currentRow) + self.numDigitSum(currentCol) > k:  # 判断当前下标的数位之和是否超过K
            return False
        return True

    # 计算一个数的数位之和
    def numDigitSum(self, num):
        index = 0
        count = 0
        while 10 ** index <= num:
            count = count + int((num / 10 ** index % 10))
            index = index + 1
        return count