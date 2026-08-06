class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        base = ord('a')

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - base] += 1
            res[tuple(count)].append(s)

        return list(res.values())