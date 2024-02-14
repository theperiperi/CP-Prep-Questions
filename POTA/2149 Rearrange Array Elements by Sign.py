class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_pointer=0
        negative_pointer=1
        result=[-1 for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]<0:
                result[negative_pointer]=nums[i]
                negative_pointer+=2
            else:
                result[positive_pointer]=nums[i]
                positive_pointer+=2
        return result        
