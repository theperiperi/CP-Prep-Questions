class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        prefix = [0] * n
        prefix[0] = nums[0]        

        for i in range(1,n):
            prefix[i] = max(prefix[i-1], nums[i])
        
        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1],nums[i])
        
        res = 0
        for i in range(1, n-1):
            left = prefix[i-1]
            right = suffix[i+1]
            res = max(res, (left-nums[i]) * right)

        return res
