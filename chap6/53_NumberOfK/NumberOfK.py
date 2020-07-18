
#思路一对应的代码
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==None or len(nums)<1:
            return 0
        count=0
        for index in range(len(nums)):
            if nums[index]==target:
                count=count+1
        return count