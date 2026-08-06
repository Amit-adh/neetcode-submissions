class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i, x in enumerate(nums):
            idx[x] = i

        for i, x in enumerate(nums):
            diff = target - x

            if diff in idx and i != idx[diff]:
                return sorted([i, idx[diff]])
            