class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        max_res = 0
        max_val = nums[0]
        max_dif = 0

        for i in range(1,n):
            max_res = max(max_res, max_dif * nums[i])
            max_dif = max(max_dif, max_val - nums[i])
            max_val = max(max_val, nums[i])

        return max_res
