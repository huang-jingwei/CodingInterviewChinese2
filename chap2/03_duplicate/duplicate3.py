class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length=len(nums)

        # step1:原数组元素范围为：0～n-1 ，将其调整至1～n
        for index in range(length):
            nums[index] +=1

        # step2：遍历数组，获得元素对应的下标index，再将index对应的元素取反
        # 若index对应的元素为负数，那么index至少已经出现一次
        for i in range(length):
            index=abs(nums[i])-1

            if nums[index]<0:
                return index
            else:
                nums[index]=-1*nums[index]