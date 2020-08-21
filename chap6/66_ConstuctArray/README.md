# 面试题66：构建乘积数组

【题目】给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

例子

```python
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
```

LeetCode:[构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)



**思路一：暴力解法**

算法时间复杂度：O(N^2)，但是暴力解法会超出时间限制。

```Python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        listLength=len(a)
   
        answer=[1]*listLength
        for index in range(listLength):
            product=1
            leftIndex=0
            while leftIndex<index:
                product *=a[leftIndex]
                leftIndex +=1
            
            rightIndex=index+1
            while rightIndex <listLength:
                product *=a[rightIndex]
                rightIndex +=1
            answer[index]=product
        return answer
```





**思路二**

算法时间复杂度：O(N)

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        listLength=len(a)
        if listLength==0:
            return []
        elif listLength==1:
            return a
   
        #left[index]:代表A[0]*A[1]*...*A[index-1]
        left=[1]*listLength  
        for index in range(1,listLength):
            left[index]=left[index-1]*a[index-1]
        
        #right[index]:代表A[index+1]*A[index+2]*...*A[listLength-1]
        right=[1]*listLength  
        for index in range(listLength-2,-1,-1):
            right[index]=right[index+1]*a[index+1]
        
        answer=[1]*listLength  
        for index in range(listLength):
            answer[index]=left[index]*right[index]
        return answer         
```

