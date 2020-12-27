class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 创建数组
        array = [[False for i in range(n)] for j in range(m)]
        self.count = 0  # 可以到达的方格的数量

        self.infet(0, 0, m, n, k, array)
        return self.count

    # 函数功能：将可以到达的方格中的数值转化为True
    # 部分参数说明：
    # rowIndex，rowIndex分别为当前数组的行列下标
    # k:行列下标之和的数值边界
    def infet(self, rowIndex, colIndex, m, n, k, array):

        # 防止数组下标越界
        if rowIndex < 0 or rowIndex >= m or colIndex < 0 or colIndex >= n:
            return
            # 该位置已经被计算过了
        elif array[rowIndex][colIndex] == True:
            return

        value = self.indexSum(rowIndex) + self.indexSum(colIndex)
        if value <= k:
            array[rowIndex][colIndex] = True
            self.count += 1
            # 继续沿着四个方向进行搜索
            self.infet(rowIndex + 1, colIndex, m, n, k, array)
            self.infet(rowIndex - 1, colIndex, m, n, k, array)
            self.infet(rowIndex, colIndex + 1, m, n, k, array)
            self.infet(rowIndex, colIndex - 1, m, n, k, array)

    # 函数功能：计算十进制数(必为非负数)的位数之和
    def indexSum(self, num):
        count = 0
        while num >= 0:
            s = int(num // 10)  # 商
            y = int(num % 10)  # 余数，即每一位的位数

            count += y
            if s == 0:
                break
            else:
                num = s
        return count