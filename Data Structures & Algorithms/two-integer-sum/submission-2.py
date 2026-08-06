class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = [target - x for x in nums]

        for idx, x in enumerate(table):
            if x in nums and nums.index(x) != idx:
                return sorted([idx, nums.index(x)])