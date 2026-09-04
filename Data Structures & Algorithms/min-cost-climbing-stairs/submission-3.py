class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        n = len(cost)
        steps = [0] * n
        steps[-1] = cost[-1]
        steps[-2] = cost[-2]

        for i in range(n-3, -1, -1):
            steps[i] = cost[i] + min(steps[i+1], steps[i+2])

        return min(steps[0], steps[1])

