class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        indices = {}
        left = 0

        for i, ch in enumerate(s):

            if ch in indices and left <= indices[ch]:
                left = indices[ch] + 1

            indices[ch] = i
            maxL = max(maxL, i - left + 1)

        return maxL