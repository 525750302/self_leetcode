import copy
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        length = len(prices)
        k = min(k, length//2)

        buy = [[0]*(k+1) for i in range(length)]
        sell = [[0]*(k+1) for i in range(length)]

        buy[0][0] = -prices[0]
        sell[0][0] = 0
        for i in range(1, k + 1):
            buy[0][i] = buy[0][i] = -9999
        
        for i in range(1, length):
            buy[i][0] = max(buy[i-1][0],sell[i-1][0] - prices[i])
            for j in range(1,k+1):
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])


        return max(sell[length-1])

    
a = Solution()
input = [[]]
result = a.maxProfit(input)
print(result)