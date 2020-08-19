# 面试题60：n个骰子的点数



【题目】把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



LeetCode:[n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

**示例** :

```python
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
    
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
```





**解题思路：分情况讨论**

1、特殊情形，五张扑克牌都是大小王，这个时候能构成顺子

2、其余情形，需要同时满足以下两个条件才能构成顺子

- 除大小王的数值0外，扑克牌中中不能出现重复数字
- 除大小王的数值0外，扑克牌的最大数值和最小数值不能差值不能大于4

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