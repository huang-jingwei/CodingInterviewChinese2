# 面试题60：n个骰子的点数



【题目】把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



LeetCode:[n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

**示例** :

```python
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
    
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```





**解题思路**

先计算在n次投递时，每个面值总和出现的次数，再来计算各个面值出现的概率。

```Python
class Solution:
    def twoSum(self, n: int) -> List[float]:
        # n次扔筛子后，可能出现面值的最大值和最小值
        s_max = n * 6
        s_min = n * 1

        # timesCount[i][j]:代表第i次扔筛子，总和为j的次数
        # 注意，初始化时，增加了第0次扔筛子和面值总和为0
        timesCount = [[0 for i in range(s_max + 1)] for j in range(n + 1)]

        for time in range(1, len(timesCount)):
            # 第一次扔筛子，面值在1~6的次数都为1
            if time == 1:
                for i in range(1, 7):
                    timesCount[time][i] = 1
                continue
            # 当投掷筛子的次数time>=2时
            time_max = time * 6  # 本次遍历的最小值和最大值
            time_min = time * 1
            for coin in range(time_min, time_max + 1):
                for i in range(1, 7):  # 单次扔筛子，面值范围为：1~6
                    if coin - i >= 0:
                        timesCount[time][coin] += timesCount[time - 1][coin - i]
        prob = timesCount[-1][s_min:]
        times_sum = sum(timesCount[-1][s_min:])
        for i in range(len(prob)):
            prob[i] = prob[i] / times_sum
        return prob
```