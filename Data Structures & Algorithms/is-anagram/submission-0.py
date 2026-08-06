class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        n = {}
        m = {}

        for i in range(len(s)):
            n[s[i]] = 1 + n.get(s[i], 0)
            m[t[i]] = 1 + m.get(t[i], 0)

        return n == m 
        