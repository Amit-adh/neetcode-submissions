class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for x in nums:
            res[x] = 1 + res.get(x, 0)
        
        counts = []
        for key, value in res.items():
            counts.append([value, key])

        counts.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(counts[i][1])

        return ans