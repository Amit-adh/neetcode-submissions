class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        m = len(s2)

        c1 = {}
        c2 = {}
        
        for ch in s1:
            c1[ch] = c1.get(ch, 0) + 1

        left = 0
        right = 0

        while right < m:
            while right - left < n:
                ch = s2[right]
                c2[ch] = c2.get(ch, 0) + 1
                right += 1

            if c1 == c2:
                return True
            else:
                c2[s2[left]] = c2.get(s2[left], 1) - 1
                if c2[s2[left]] == 0:
                    c2.pop(s2[left])
                left += 1
        
        return False