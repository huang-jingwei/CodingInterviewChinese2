

#函数功能：找出旋转数组的最小数字
#思路一 解题思路：遍历数组,找出数组的最小值
#算法复杂度:O(N)

def MinNumberInRotatedArray_way1(array):
    if array==None or len(array)==0:   #判断数组是否为空数组
        return None
    minValue=array[0]                  #初始化数组的最小值
    for index in range(1,len(array)):
        if array[index]<minValue:
            minValue=array[index]
    return minValue

#函数功能：找出旋转数组的最小数字
#思路二 解题思路：二分查找
#算法复杂度:O(log N)

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0  # 数组的左右边界
        right = len(numbers) - 1

        # 旋转后数组可分为：左有序数组(数值相对大)+右有序数组(数值相对小)
        # 原问题可变为，数组的最小值为右有序数组的第一个元素

        # 特别注意，进行二分计算时，要防止左右边界越界

        while left < right:
            mid = (left + right) // 2

            # 情况1：若numbers[mid]<numbers[right]，则mid必定在右有序数组，right指针左移
            if numbers[mid] < numbers[right]:
                right = mid
            # 情况2：若numbers[mid]>numbers[right]，则mid必定在左有序数组，left指针右移
            elif numbers[mid] > numbers[right]:
                left = min(mid + 1, right)
            # 情况3：若numbers[mid]=numbers[right]，不确定mid在哪个有序数组，right指针左移
            elif numbers[mid] == numbers[right]:
                right -= 1
        return numbers[left]