# 面试题45. 把数组排成最小的数



【题目】 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。



LeetCode:[剑指 Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)



 **示例** 

```python
输入: [10,2]
输出: "102"

输入: [3,30,34,5,9]
输出: "3033459"
```



**提示:**

- 0 < nums.length <= 100

**说明:**

- 输出结果可能非常大，所以你需要返回一个字符串而不是整数
- 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0





**思路一：暴力dfs**

最简单直接的方法就是用dfs的方法对所有可能出现的数字进行比较，选出最小的数字。

算法时间复杂度：O(N^2)

这种方法会超出时间限制

```Python
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        length=len(nums)     # 数组长度
        pb=[False]*length    # 布尔数组，记录当前位置数字是否已加入
      
        if length==1:        # 数组只有一个数字时，直接返回
            return nums[0]
        
        self.result=float("inf")
        self.dfs(nums,length,0,pb,[])
        return self.result
    

    def dfs(self,nums,length,index,pb,arr):
        if index==length:
            res=("").join(arr)
            if self.result==float("inf"):
                self.result=res
            else:
                if int(res)<int(self.result):
                    self.result=res
            return
        
        for i in range(length):
            if pb[i]==False:
                pb[i]=True
                arr.append(str(nums[i]))
                self.dfs(nums,length,index+1,pb,arr)
                pb[i]=False
                arr.pop()
```











