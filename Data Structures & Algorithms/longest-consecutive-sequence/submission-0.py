class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        starts = {}
        set_nums = set(nums)

        for num in set_nums:
            starts[num] = 1

        longest = 0
        for num in starts:
            if num -1 not in starts:
                length = 1
                while num + length in starts:
                    length += 1

                longest = max(longest, length)

        return longest