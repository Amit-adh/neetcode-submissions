class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        
        first = nums[0]
        second = max(nums[0], nums[1])
        self.max = max(first, second)

        for i in range(2, n):
            curr = max(second, first + nums[i])
            self.max = max(self.max, curr)

            first = second
            second = curr

        return self.max