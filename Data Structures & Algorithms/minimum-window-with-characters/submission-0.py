class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        m = len(s)
        n = len(t)

        left = 0
        right = 0

        c1 = {}
        c2 = {}

        for ch in t:
            c1[ch] = c1.get(ch, 0) + 1
        
        need = len(c1)
        have = 0
        
        minlen = m
        minL = 0
        minR = 0
        found = False

        while right < m:
            while right < m and have != need:
                ch = s[right]
                if ch in c1:
                    c2[ch] = c2.get(ch, 0) + 1
                    if c2.get(ch) == c1.get(ch):
                        have += 1

                right += 1
            
            while left < m and have == need:

                if have == need and right - left <= minlen:
                    minL = left
                    minR = right - 1
                    minlen = right - left
                    found = True

                ch = s[left]
                if ch in c1:
                    c2[ch] -= 1

                    if c1.get(ch) > c2.get(ch):
                        have -= 1

                left += 1

        if found:
            return s[minL: minR + 1]
        return ""