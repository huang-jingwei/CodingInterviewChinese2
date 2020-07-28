#函数功能：题目一的思路一，数组中数字出现的次数
#基本思路：哈希表
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        number = []  # 存放出现两次的数字
        data = {}    # 用字典来模拟哈希表结构
        for index in range(len(nums)):
            if nums[index] not in data:
                data[nums[index]] = 1
            else:
                data[nums[index]] += 1

        for num, times in data.items():
            if times != 2:
                number.append(num)
        return number