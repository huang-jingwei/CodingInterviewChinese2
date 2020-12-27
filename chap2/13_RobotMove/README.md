# 面试题13：机器人的运动范围



【题目】地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。

【例如】当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



LeetCode:[机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)



借鉴岛问题的解法进行求解该问题

【LeetCode相关问题链接】[岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

有道笔记链接：[第7讲.note](http://note.youdao.com/noteshare?id=1ab8a0c3be6a757f2dd1005184110412&sub=317924FCBB884FFD909849052C1A689E)


```python
class Solution: 
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 创建数组
        array=[[False for i in range(n)] for j in range(m)]
        self.count=0    #可以到达的方格的数量
        
        self.infet(0,0,m,n,k,array)
        return self.count
    

    # 函数功能：将可以到达的方格中的数值转化为True
    # 部分参数说明：
    # rowIndex，rowIndex分别为当前数组的行列下标
    # k:行列下标之和的数值边界
    def infet(self,rowIndex,colIndex,m,n,k,array):

        # 防止数组下标越界
        if rowIndex<0 or rowIndex>=m or colIndex<0 or colIndex>=n:
            return 
        # 该位置已经被计算过了
        elif array[rowIndex][colIndex]==True:
            return
        
        value=self.indexSum(rowIndex)+self.indexSum(colIndex)
        if value<=k:
            array[rowIndex][colIndex]=True
            self.count+=1
            # 继续沿着四个方向进行搜索
            self.infet(rowIndex+1,colIndex,m,n,k,array)
            self.infet(rowIndex-1,colIndex,m,n,k,array)
            self.infet(rowIndex,colIndex+1,m,n,k,array)
            self.infet(rowIndex,colIndex-1,m,n,k,array)


    # 函数功能：计算十进制数(必为非负数)的位数之和
    def indexSum(self,num):
        count=0
        while num>=0:
            s =int(num //10) #商
            y=int(num % 10)  #余数，即每一位的位数

            count +=y
            if s==0:
                break
            else:
                num=s
        return count
```




