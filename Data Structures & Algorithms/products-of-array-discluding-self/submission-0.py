class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        left = 1
        while left < len(nums):
            prefix[left] = nums[left-1] * prefix[left - 1]
            left += 1

        right = len(nums) - 2
        while right >= 0:
            suffix[right] = nums[right + 1] * suffix[right + 1]
            right -= 1

        prod = [prefix[i] * suffix[i] for i in range(len(nums))]
        return prod
        