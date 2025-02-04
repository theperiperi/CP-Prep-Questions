class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        local_sum = nums[0]
        max_sum = local_sum

        for num in range(len(nums) - 1) :
            if nums[num]< nums[num+1]:
                local_sum+=nums[num+1]
                max_sum = max(local_sum, max_sum)
            else:
                local_sum = nums[num+1]
            print(local_sum, max_sum)

        return max_sum
        
