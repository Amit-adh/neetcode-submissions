class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        
        counter = {}
        l = 0
        r = 0
        maxL = 0


        while r < len(s):
            ch = s[r]
            counter[ch] = counter.get(ch, 0) + 1
            r += 1

            window_size = r - l
            maxF = 0
            for c in counter:
                maxF = max(maxF, counter.get(c))

            if window_size - maxF <= k:
                maxL = max(maxL, window_size)
            else:
                c = s[l]
                counter[c] = counter.get(c) - 1
                l += 1
        
        return maxL