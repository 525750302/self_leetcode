class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        length = len(prices)

        buy = [0 for i in range(length)]
        sell = [0 for i in range(length)]

        for i in range(length):
            buy[i] = -99999
            sell[i] = -99999
            
        buy[0] = -prices[0]
        if len(prices)>1:
            buy[1] = max(buy[0],-prices[1])
            sell[1] = max(0,prices[1] - prices[0])
        sell[0] = 0
        for i in range(2,length):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])


        return max(sell)