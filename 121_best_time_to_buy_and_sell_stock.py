class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #edge cases
        
        max_sell_prices = [0 for i in range(len(prices))]
        max_this_far = 0
        max_profit = 0
        
        for i in range(len(prices)-1,-1,-1):
            if prices[i] > max_this_far:
                max_this_far = prices[i]
                
            max_sell_prices[i] = max_this_far
        
        for i in range(len(prices)):
            profit = max_sell_prices[i] - prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit
