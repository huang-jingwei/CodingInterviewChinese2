# 面试题59：队列的最大值



【题目一】 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。



**例如**

```python
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```



LeetCode:[滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)



**解题思路：单调栈**

算法时间复杂度：O(N)

```Python
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
```



【题目二】请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1



**例如**

```Python
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
```



```python
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
```



LeetCode:[队列的最大值](https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/)





