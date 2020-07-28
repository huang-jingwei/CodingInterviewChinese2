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