class Solution:
    def numWays(self, n: int) -> int:
        if n<=1:
            return 1

        count=[0]*(n+1)
        count[0]=1
        count[1]=1
        for index in range(2,n+1):
            count[index]=count[index-1]+count[index-2]
            if count[index]>1000000007:
                count[index]=count[index] %(1000000007)
        return count[-1]