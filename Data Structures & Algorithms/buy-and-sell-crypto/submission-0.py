class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStocks = []
        
        min = 101

        for x in prices:
            if x < min:
                min = x
            minStocks.append(min)

        prof = [prices[i] - minStocks[i] for i in range(len(prices))]

        m = max(prof)
        if m > 0:
            return m
        else:
            return 0