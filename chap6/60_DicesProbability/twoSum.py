class Solution:
    def twoSum(self, n: int) -> List[float]:
        s_max = n * 6  # n次扔筛子后，可能出现面值的最大值和最小值
        s_min = n * 1

        # timesCount[i][j]:代表第i次扔筛子，总和为j的次数
        # 注意，增加了第0次扔筛子和面值总和为0
        timesCount = [[0 for i in range(s_max + 1)] for j in range(n + 1)]

        for time in range(1):
            time_max = time * 6  # 本次遍历的最小值和最大值
            time_min = time * 1
            for coin in range(time_min, time_max + 1):
                for i in range(1, 7):  # 单次扔筛子，面值范围为：1~6
                    if coin - i >= 0:
                        timesCount[time][coin] += timesCount[time - 1][coin - i] + 1

        prob = timesCount[-1][s_min:]
        times_sum = sum(timesCount[-1][s_min:])
        for i in range(len(prob)):
            prob[i] = prob[i] / times_sum
        return prob