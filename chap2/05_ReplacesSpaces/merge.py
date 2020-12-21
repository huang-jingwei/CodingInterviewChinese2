class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)  # num1数组长度
        # 采用类外排法进行合并数组，排序顺序是从大排序到小
        index1 = m - 1  # 两个数组的移动下标
        index2 = n - 1
        index = length - 1  # 合并数组的移动下标

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1
        # 至少一个数组被遍历结束
        if index1 >= 0:
            while index1 >= 0:
                nums1[index] = nums1[index1]
                index1 -= 1
                index -= 1
        elif index2 >= 0:
            while index2 >= 0:
                nums1[index] = nums2[index2]
                index2 -= 1
                index -= 1

        # 若num1的初始化空间大于m+n，即此时index>0
        # 将已经排序好的num1数组数值元素向前移动index个位置，剩余的位置全部置0
        if m + n < length:
            # num1数组初始化时多出的空间，即
            # num1数组需要置0的区间的长度
            gap = length - m - n

            for i in range(m + n):
                nums1[i] = nums1[i + gap]
            for j in range(m + n, length):
                nums1[j] = 0