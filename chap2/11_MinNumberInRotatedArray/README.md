# 面试题11：旋转数组的最小数字



【题目】把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减序列的一个旋转，输出旋转数组的最小元素。



【例如】数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。



LeetCode:[旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)



**思路一：遍历实现**

算法时间复杂度：O（N）

```python
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
```



**思路二：二分查找**

【分析】旋转后数组可分为：左有序数组(数值相对大)+右有序数组(数值相对小)，那么 原问题可变为，数组的最小值为右有序数组的第一个元素

算法时间复杂度：O（log N）



算法流程：
初始化： 声明 left, right双指针分别指向 nums数组左右两端；
循环二分： 设 mid = (left +right) / 2为每次二分的中点（ "/" 代表向下取整除法，因此恒有 left <= mid  <=right ），可分为以下三种情况：

1. 当 nums[mid ] > nums[right]时： mid 一定在 左排序数组 中，即 最小元素一定在[mid+1,right]闭区间内，因此执行 left = min(mid+1,right)；

2. 当 nums[mid] < nums[right]时： mid一定在 右排序数组 中，即最小元素一定在[left,mid]闭区间内，因此执行right=mid；

3. 当 nums[mid] = nums[right]时： 无法判断 mid在哪个排序数组中，即无法判断最小元素 在[left,mid] 还是[mid+1,right]区间中。解决方案： 执行 right = right- 1缩小判断范围

   返回值： 当 left=right时跳出二分循环，并返回 旋转点的值 nums[left] 即可。

   特别注意，要防止数组左右边界越界





```python
#函数功能：找出旋转数组的最小数字
#思路二 解题思路：二分查找
#算法复杂度:O(log N)

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left=0                # 数组的左右边界
        right=len(numbers)-1

        # 旋转后数组可分为：左有序数组(数值相对大)+右有序数组(数值相对小)
        # 原问题可变为，数组的最小值为右有序数组的第一个元素

        # 特别注意，进行二分计算时，要防止左右边界越界
        
        while left<right:
            mid=(left+right)//2

            # 情况1：若numbers[mid]<numbers[right]，则mid必定在右有序数组，right指针左移
            if numbers[mid]<numbers[right]:
                right=mid
            # 情况2：若numbers[mid]>numbers[right]，则mid必定在左有序数组，left指针右移
            elif numbers[mid]>numbers[right]:
                left=min(mid+1,right)
            # 情况3：若numbers[mid]=numbers[right]，不确定mid在哪个有序数组，right指针左移
            elif numbers[mid]==numbers[right]:
                right -=1 
        return numbers[left]
```












