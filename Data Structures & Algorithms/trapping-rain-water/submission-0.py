class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]
        
        max_h = 0
        for idx, x in enumerate(height):
            if x > max_h:
                max_h = x
            prefix[idx] = max_h

        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_h:
                max_h = height[i]
            suffix[i] = max_h

        sums = 0
        for i in range(1, len(height) - 1):
            h = min(prefix[i], suffix[i])
            sums += h - height[i]
        return sums
