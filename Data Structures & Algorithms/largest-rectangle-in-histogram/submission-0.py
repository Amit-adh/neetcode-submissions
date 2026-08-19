class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        maxA = 0
        n = len(heights)
        indices = []
        tops = []

        i = 0
        while i < n:
            if not tops or heights[i] >= tops[-1]:
                indices.append(i)

            else:
                idx = None
                while tops and heights[i] < tops[-1]:
                    width = i - indices[-1]
                    area = tops[-1] * width
                    maxA = max(maxA, area)
                    
                    tops.pop()
                    idx = indices.pop()
                
                indices.append(idx)
            
            tops.append(heights[i])
            i += 1

        while tops:
            h = tops.pop()
            w = n - indices.pop()
            area = h * w

            maxA = max(maxA, area)

        return maxA