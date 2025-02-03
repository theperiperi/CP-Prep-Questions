class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        local = 1
        res = 1
        n = len(nums)
        
        if n <= 1:
            return 1

        sign = None
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if sign != 1:
                    local = 2  
                    sign = 1
                else:
                    local += 1

            elif nums[i] < nums[i-1]:
                if sign != 0:
                    local = 2
                    sign = 0
                else:
                    local += 1
            else:
                local = 1
                sign = None

            res = max(res, local)
        return res
