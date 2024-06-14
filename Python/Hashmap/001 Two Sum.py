class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            if (target-nums[i]) in nums:
                index=nums.index(target-nums[i])
                if i==index:
                    count=nums.count(nums[i])
                    if count>1:
                        ele=nums[i]
                        nums[i]=-1
                        index=nums.index(ele)
                        break
                else:
                    break
                    
        return [i,index]
