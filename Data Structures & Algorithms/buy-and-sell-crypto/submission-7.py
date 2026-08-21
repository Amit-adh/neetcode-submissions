class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minX = prices[0]
        maxP = 0

        for x in prices:
            maxP = max(maxP, x - minX)
            minX = min(minX, x)
        return maxP