class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        
        maxA = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            maxH = min(heights[left], heights[right])
            length = right - left 
            area = maxH * length
            maxA = max(area, maxA)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxA

        