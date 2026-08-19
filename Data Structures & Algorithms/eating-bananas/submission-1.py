class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        
        left = 1
        right = n
        min_rate = n

        while left <= right:
            mid = left + (right - left) // 2

            t = 0
            for x in piles:
                t += math.ceil(x / mid)

            if t <= h:
                min_rate = min(mid, min_rate)
                right = mid - 1
            
            else:
                left = mid + 1

        return min_rate