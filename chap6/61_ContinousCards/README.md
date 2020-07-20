<<<<<<< HEAD
<<<<<<< HEAD
# 面试题61：扑克牌中的顺子

【题目】 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
=======
# 面试题61： 扑克牌中的顺子
=======
# 面试题61： 扑克牌中的顺子

【题目】从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0

【题目】从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0


<<<<<<< HEAD

LeetCode:[扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

<<<<<<< HEAD
**示例** :

```python
输入: [1,2,3,4,5]
输出: True
    
输入: [0,0,1,2,5]
输出: True
```
=======
解题思路：分情况讨论

1、特殊情形，五张扑克牌都是大小王，这个时候能构成顺子

2、其余情形，需要同时满足以下两个条件才能构成顺子

- 除大小王的数值0外，扑克牌中中不能出现重复数字
- 除大小王的数值0外，扑克牌的最大数值和最小数值不能差值不能大于4
>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0


=======
LeetCode:[扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

解题思路：分情况讨论

1、特殊情形，五张扑克牌都是大小王，这个时候能构成顺子

2、其余情形，需要同时满足以下两个条件才能构成顺子

- 除大小王的数值0外，扑克牌中中不能出现重复数字
- 除大小王的数值0外，扑克牌的最大数值和最小数值不能差值不能大于4


>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0



```Python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        List = sorted(nums)      # 对输入数组进行升序排序
        if List[0] == List[-1]:  # 特殊情形下，五张牌都是大小王
            return True

        data = {}  # 用来记录每个扑克牌出现的次数

        # 其他情形
        # 除大小王的数值0外，顺子中不能出现重复数字
        # 除大小王的数值0外，最大数值和最小数值不能差值不能大于4

        maxValue = 0  # 初始化这五张扑克牌的最大值和最小值
        minValue = 13

        for index in range(len(List)):

            if List[index] <= minValue and List[index] != 0:  # 更新扑克牌的最大值和最小值
                minValue = List[index]
            if List[index] >= maxValue and List[index] != 0:
                maxValue = List[index]

            if List[index] not in data:                      # 用字典存放扑克牌出现的次数
                data[List[index]] = 1
            elif List[index] != 0 and List[index] in data:  # 存在非0的重复数字，不可能存在顺子
                return False
            elif List[index] == 0 and List[index] in data:  # 出现多张大小王
                data[List[index]] += 1
        if maxValue - minValue > 4:                         
            return False
        else:
            return True

```





<<<<<<< HEAD
<<<<<<< HEAD
=======


>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0
=======


>>>>>>> 9b3f2264242563f0f2b34b11afca03fbd07fabd0


