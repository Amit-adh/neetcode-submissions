class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = n - 1
        
        def search(l, r):
            while l <= r:
                m = l + (r - l) // 2
                
                if nums[m] == target:
                    return m
                
                elif nums[m] > target:
                    r = m - 1

                else:
                    l = m + 1

            return -1


        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        
        if target >= nums[left] and target <= nums[n-1]:
            return search(left, n - 1)

        return search(0, left - 1)