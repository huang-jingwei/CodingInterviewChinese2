class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            while nums[i] !=i:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[i],nums[temp]=nums[temp],nums[i]