class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        List = sorted(nums)      # 对输入数组进行升序排序
        if List[0] == List[-1]:  # 特殊情形下，五张牌都是大小王
            return True

        data = {}  # 用来记录每个扑克牌出现的次数

        # 其他情形
        # 除大小王的数值0外，顺子中不能出现重复数字
        # 除大小王的数值0外，最大数值和最小数值不能差值不能大于4

        maxValue = 0  # 初始化这五张扑克牌的最大值和最小值
        minValue = 13

        for index in range(len(List)):

            if List[index] <= minValue and List[index] != 0:  # 更新扑克牌的最大值和最小值
                minValue = List[index]
            if List[index] >= maxValue and List[index] != 0:
                maxValue = List[index]

            if List[index] not in data:                      # 用字典存放扑克牌出现的次数
                data[List[index]] = 1
            elif List[index] != 0 and List[index] in data:  # 存在非0的重复数字，不可能存在顺子
                return False
            elif List[index] == 0 and List[index] in data:  # 出现多张大小王
                data[List[index]] += 1
        if maxValue - minValue > 4:
            return False
        else:
            return True
