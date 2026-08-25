class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        maxes = []
        window = deque()

        left = 0
        right = 0
        n = len(nums)

        while right < n:
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            while left > window[0]:
                window.popleft()

            if right + 1 >= k:
                maxes.append(nums[window[0]])
                left += 1

            right += 1

            
        return maxes