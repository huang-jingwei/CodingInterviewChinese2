class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexStack = []
        printArray = []

        for index in range(len(nums)):
            while len(indexStack) > 0 and nums[index] >= nums[indexStack[-1]]:
                indexStack.pop()
            indexStack.append(index)

            if index - indexStack[0] == k:
                indexStack.pop(0)

            if index >= k - 1:
                printArray.append(nums[indexStack[0]])
        return printArray