class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        closest_sum=float('inf')

        for number in range(n-2):
            left=number+1
            right=n-1
            while left<right:
                current_sum=nums[number]+nums[left]+nums[right]
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                
                if current_sum<target:
                    left+=1
                elif current_sum> target:
                    right-=1
                else:
                    return closest_sum
        return closest_sum
        
