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

            maxF = 0
            for c in counter:
                maxF = max(maxF, counter.get(c))

            window = r-l

            if window - maxF <= k:
                maxL = max(maxL, window)
            else:
                ch = s[l]
                counter[ch] = counter.get(ch, 1) - 1
                l += 1

        return maxL


            

            