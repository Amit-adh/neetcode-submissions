class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        left = 0
        right = 0
        maxes = []
        window = deque()

        while right < len(nums):
            
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            right += 1

            if left > window[0]:
                window.popleft()

            if right + 1 > k:
                maxes.append(nums[window[0]])
                left += 1


        return maxes