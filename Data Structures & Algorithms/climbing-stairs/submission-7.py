class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        a = 1
        b = 1

        for i in range(n):
            steps = a + b
            a = b
            b = steps

        return a


