# 面试题3：数组中重复的数字

**题目：** 在一个长度为n的数组里的所有数字都在0~n-1的范围内。数组中某些数字是重复的，但不知道有几个数字是重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。



**例如：** 输入长度为7的数组{2,3,1,0,2,5,3}，那么对于的输出是重复的数字2或者3.



LeetCode:[数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)



**思路一：对数组进行排序**

时间复杂度：O(N*log N)

先把输入的数组间排序。从排序额数组中国找出重复的数值是一件容易的事情，只需要从头到尾扫描排序后的数值即可。

```python
def duplicate_right(array):
    if array==None or len(array)<=0:    #判断数组是否为空数组
        return None
    sortArray=sorted(array)
    for index in range(len(sortArray)-1):
        if sortArray[index]==sortArray[index+1]:
            return sortArray[index]
    return False
```

**思路二：哈希表**

时间复杂度：O(N)

采用哈希表来解决这个问题。从头到尾按顺序来扫描数组的每个数字，每扫描到一个数字的时候，都可以用O(1)的时间来判断哈希表里是否包含了这个数组。如果哈希表里面没有这个数字，就报它加入哈希表。如果哈希表里已经存在该数字，就找到一个重复的数字。

弊端：

这个算法的时间复杂度是O(N)，但它提高时间效率是以一个大小为O(N)的哈希表为代价。

```python
#函数功能：找出数组中重复的数字
#思路二：基于哈希表
#算法复杂度:O(N)
def duplicate(array):
    if array==None or len(array)<=0:    #判断数组是否为空数组
        return None
    hashMap={}                          #用来记录数组中元素是否是重复元素
    for index in range(len(array)):
        if array[index] not in hashMap: #若字典中没存在该元素，则将该元素添加到字典中
            hashMap[array[index]]=1
        else:                           #若字典中已经存在该元素，则直接返回
            return array[index]
```



**思路三：遍历数组，对对应位置进行取反**

题目分析：因为数组 nums 里的所有数字都在 0～n-1 的范围

1、遍历nums数组，每个数组元素num[i]都对应一个下标index，对num[index]进行取反操作；

2、在进行取反操作前，若num[index]对应的元素为负数，那么num[index]之前至少已经进行一次取反操作，则index就是重复出现的数字。



这个算法的时间复杂度是O(N)，空间复杂度O(1)。



```python
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
```



**思路四：原地哈希**

第三种方法可看作原地哈希，不过没有用到字典。具体做法就是因为题目中给的元素是 < len（nums）的，所以我们可以让 位置i 的地方放元素i。

可以看做是一种原地哈希，不过没有用到字典。具体做法就是因为题目中给的元素是 < len（nums）的，所以我们可以让 位置i 的地方放元素i。

- 如果位置i的元素不是i的话，那么我们就把i元素的位置放到它应该在的位置，即 nums[i] 和nums[nums[i]]的元素交换，这样就把原来在nums[i]的元素正确归位了。
- 如果发现 要把 nums[i]正确归位的时候，发现nums[i]（这个nums[i]是下标）那个位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return

**算法复杂度**：时间复杂度O(n)，空间复杂度O(1)。

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            while nums[i] !=i:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[i],nums[temp]=nums[temp],nums[i]   
```

