
# 函数功能： 找出股票的最大利润
#基本思路：暴力解法，算法时间复杂度O(N^2)
# 搜索当前时间节点后的全部节点，找出股票收入最大的节点。
# 然后拿股票收入最大与当前的收入做比较，若比当前股票收入大，那么就产生利润，
# 并且此时的利润为最大利润。否则不交易股票，不产生利润。
def MaximalProfit_right1(array):
    if array==None or len(array)<2:
        return 0
    maxProfit=0
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[j]-array[i]>=maxProfit:
                maxProfit=array[j]-array[i]
    return maxProfit


#函数功能： 找出股票的最大利润
#基本思路：思路二，算法时间复杂度：O(N)
#记录当前节点前的股票收入最小值minPrePrices，那么当前股票收入prices[i]
#和minPrePrices之间的差值就是当前能获取的最大利润
def maxProfit(prices) :
    if prices ==None or len(prices ) < 2:
        return 0
    minPrePrices = prices[0]                     # 记录当前节点前的股票最小值
    maxProfit = 0                                # 股票收入最大利润
    for i in range(len(prices)):
        if prices[i] <= minPrePrices:            # 更新当前节点前的股票最小值
            minPrePrices = prices[i]
        if prices[i] - minPrePrices >= maxProfit: # 更新股票最大收入
            maxProfit = prices[i] - minPrePrices
    return maxProfit