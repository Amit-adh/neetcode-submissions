class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binary(m, left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if matrix[m][mid] == target:
                    return True

                elif matrix[m][mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1
            
            return False

        if m == 1:
            return binary(0, 0, n-1)

        left_m = 0
        right_m = m - 1

        while left_m <= right_m:
            mid_m = left_m + (right_m - left_m) // 2

            if target >= matrix[mid_m][0]:
                if target <= matrix[mid_m][-1]:
                    return binary(mid_m, 0, n-1)
                
                else:
                    left_m = mid_m + 1

            else:
                if target >= matrix[mid_m - 1][0]:
                    return binary(mid_m - 1, 0, n-1)
                right_m = mid_m - 1

        return False