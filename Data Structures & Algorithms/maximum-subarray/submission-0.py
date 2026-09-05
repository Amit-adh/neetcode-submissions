class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxS = float("-inf")
        curr = 0

        for n in nums:
            curr += n

            maxS = max(maxS, curr)
            if curr < 0:
                curr = 0

        return maxS