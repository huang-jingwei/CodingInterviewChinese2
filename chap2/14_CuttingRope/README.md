# 面试题14：剪绳子



【题目】给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。



【例如】

```Python
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```



```Python
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```



LeetCode:[剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)



采用动态规划求解该问题。下面两种方法都是采用动态规划来求解这个问题，推荐方法1.

方法1

```Python
class Solution2:
    def cuttingRope(self, n: int) -> int:
        if n == 1:  # 1米总长的绳子最大乘积为1
            return 1

        # waysCut[i]：代表i米的绳子可生成的最大乘积
        # 0米总长的绳子的最大乘积为0,1米总长的绳子最大乘积为1
        waysCut = [0] * (n + 1)
        waysCut[0] = 1

        # 采用动态规划方法，从小到大依次遍历各个总长度的绳子
        for length in range(2, n + 1):

            # 将绳子的长度分为两大段：subLength和length-subLength 
            # 然后分别计算这两大段的最大乘积，再将他们的最大乘积相乘就是最后的最大乘积
            for subLength in range(1, length):
                # 再来考虑对这两大段是否还要继续划分
                maxLength1 = max(subLength, waysCut[subLength])
                maxLength2 = max(length - subLength, waysCut[length - subLength])
                # maxLength1*maxLength2代表两大段的最大乘积
                waysCut[length] = max(waysCut[length], maxLength1 * maxLength2)
        return waysCut[-1]
```



方法2

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        #根据题意，绳子要至少切一刀
        # 1.任取长度为n的绳子，我们可以切最多n-1刀，现在考虑切的第一刀，有n-1种切法
        # 2.那么用dp[n]表示长度为n的绳子可以产生的最大乘积
        # 由1可知，dp[n] = max(dp[i]*dp[n-i]),i属于[1,n-1]
        # 初始化边界是本题比较狗血的，因为i = 2,3的时候，dp的结果为1,2.但是在其他节点中，他们应该是2 3

        if n==2:
            return 1
        elif n==3:
            return 2
        else:
            dp=[0]*(n+1)
            for index in range(len(dp)):
                dp[index]=index
            for length in range(4,len(dp)):
                for j in range(1,length):
                    dp[length]=max(dp[length],j*dp[length-j])
            return dp[-1]
```




