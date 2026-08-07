class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            
        nums.sort()
        p1 = 0
        res = []
        
        while p1 < len(nums) - 2:
            target =  -1 * nums[p1]
            
            p2 = p1 + 1
            p3 = len(nums) - 1

            while p2 < p3:
                if nums[p2] + nums[p3] == target:
                    res.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1

                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1
                    while p3 > p2 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1
                    

                elif nums[p2] + nums[p3] > target:
                    p3 -= 1
                else:
                    p2 += 1
            
            while p1 < len(nums) - 2 and nums[p1+1] == nums[p1]:
                p1 += 1
            p1 += 1

        return res