class Solution:
    def minNumber(self, nums: List[int]) -> str:
        length = len(nums)  # 数组长度
        pb = [False] * length  # 布尔数组，记录当前位置数字是否已加入

        if length == 1:  # 数组只有一个数字时，直接返回
            return nums[0]

        self.result = float("inf")
        self.dfs(nums, length, 0, pb, [])
        return self.result

    def dfs(self, nums, length, index, pb, arr):
        if index == length:
            res = ("").join(arr)
            if self.result == float("inf"):
                self.result = res
            else:
                if int(res) < int(self.result):
                    self.result = res
            return

        for i in range(length):
            if pb[i] == False:
                pb[i] = True
                arr.append(str(nums[i]))
                self.dfs(nums, length, index + 1, pb, arr)
                pb[i] = False
                arr.pop()