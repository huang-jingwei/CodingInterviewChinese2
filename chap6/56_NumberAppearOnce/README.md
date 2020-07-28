# 面试题56：数组中数字出现的次数

【题目一】一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。



LeetCode:[数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)



**思路一：暴力解法**

最简单直接的方法就是用一个哈希表来存放数组中不同数值元素出现的次数。缺点是空间复杂度是O(n)。

```Python
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
```



**思路二：异或**

算法时间复杂度：O(N)，空间复杂度是O(1)

```python

```


