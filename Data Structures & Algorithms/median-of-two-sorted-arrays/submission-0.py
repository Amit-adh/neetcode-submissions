class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        n = len(B)

        half = (m + n) // 2

        l = 0
        r = m - 1

        while True:
            A_mid = l + (r - l) // 2
            B_mid = half - A_mid - 2

            A_l = A[A_mid] if A_mid >= 0 else float("-infinity")
            A_r = A[A_mid + 1] if A_mid + 1 < m else float("infinity")
            B_l = B[B_mid] if B_mid >= 0 else float("-infinity")
            B_r = B[B_mid + 1] if B_mid + 1 < n else float("infinity")

            if A_l <= B_r and B_l <= A_r:
                if (m + n) % 2 == 0:
                    l_max = max(A_l, B_l)
                    r_min = min(A_r, B_r)

                    return float( (l_max + r_min) / 2)
                else:
                    return min(A_r, B_r)
            elif A_l > B_r:
                r = A_mid - 1
            else:
                l = A_mid + 1