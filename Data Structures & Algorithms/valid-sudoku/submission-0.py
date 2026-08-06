class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def hasDuplicates(nums: List[str]) -> bool:
            return len(nums) != len(set(nums))

        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        sqrs = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                x = board[i][j]

                if x.isalnum():
                    rows[i].append(x)
                    cols[j].append(x)
                    sqrs[3 * (i//3) + (j//3)].append(x)

        for row in rows:
            if hasDuplicates(row):
                return False
        for col in cols:
            if hasDuplicates(col):
                return False
        for sqr in sqrs:
            if hasDuplicates(sqr):
                return False

        return True
