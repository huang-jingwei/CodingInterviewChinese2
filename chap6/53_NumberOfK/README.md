# 面试题53：在排序数组中查找数字



【题目】 统计一个数字在排序数组中出现的次数。

例如：统计一个数字在排序数组中出现的次数。例如，输入排序数组{1、2、3、3、3、3、4、5}和数字3，由于3在这个数组中出现了4次，因此输出4



**思路一：暴力解法**

最简单直接的方法就是每扫描到一个数字，逐个比较该数字和它后面的数字的大小。如果后面的数字比他小，则两个数字组成一个逆序对。

算法时间复杂度：O(N)

LeetCode:[在排序数组中查找数字](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)

```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==None or len(nums)<1:
            return 0
        count=0
        for index in range(len(nums)):
            if nums[index]==target:
                count=count+1
        return count
```



**思路二：二分查找**

LeetCode:[在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

采用二分法进行搜索

```python
#思路二对应的代码
import copy

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) < 1:  # 输入列表没有元素时
            return [-1, -1]
        elif len(nums) == 1 and nums[0] == target:  # 输入列表只有一个元素时
            return [0, 0]

        # 先判断数组中是否存在该数字
        # 若该数组不存在目标数字，直接返回[-1,-1]
        # 若该数字存在目标数字，则先返回数字出现的下标
        inedx = self.binarySearch(array=nums, leftIndex=0, rightIndex=len(nums) - 1, target=target)
        if inedx == -1:
            return [-1, -1]

        # 再沿着上面步骤所得数字的下标，沿着左方向继续搜索，直到找到数字出现的左边界为止
        left = copy.copy(inedx)
        while left - 1 >= 0 and nums[left - 1] == target:
            left = self.binarySearch(array=nums, leftIndex=0, rightIndex=left - 1, target=target)

        # 再沿着上面步骤所得数字的下标，沿着右方向继续搜索，直到找到数字出现的右边界为止
        right = copy.copy(inedx)
        while right + 1 <= len(nums) - 1 and nums[right + 1] == target:
            right = self.binarySearch(array=nums, leftIndex=right + 1, rightIndex=len(nums) - 1, target=target)
        return [left, right]

    # 二分查找
    def binarySearch(self, array, leftIndex, rightIndex, target):
        while leftIndex <= rightIndex:
            # 搜索区间只剩下一个元素时
            if leftIndex == rightIndex and array[leftIndex] == target:
                return leftIndex
            elif leftIndex == rightIndex and array[leftIndex] != target:
                return -1

            # 搜索区间存在多个元素时
            if leftIndex < rightIndex:
                mid = leftIndex + (rightIndex - leftIndex) // 2  # 搜索区间的中间点
                if array[mid] == target:  # 搜索区间的中间点数组等于目标元素，直接返回
                    return mid
                elif array[mid] < target:  # 搜索区间的中间点数组小于目标元素，在右子区间进行下一轮搜索
                    leftIndex = mid + 1
                elif array[mid] > target:  # 搜索区间的中间点数组大于目标元素，在左子区间进行下一轮搜索
                    rightIndex = mid - 1
        return -1
```



