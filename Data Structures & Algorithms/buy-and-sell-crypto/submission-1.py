class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStocks = []
        
        min = 101

        for idx, x in enumerate(prices):
            if x < min:
                min = x
            prices[idx] -= min

        # prof = [prices[i] - minStocks[i] for i in range(len(prices))]

        m = max(prices)
        if m > 0:
            return m
        else:
            return 0