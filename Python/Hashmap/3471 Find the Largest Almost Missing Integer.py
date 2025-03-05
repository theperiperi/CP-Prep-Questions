class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        if k==1:
            counter = Counter(nums)
            unique = [k for k,v in counter.items() if v==1]
            if len(unique) == 0:
                return -1
            return max(unique)
        
        counter1 = nums.count(nums[0])
        counter2 = nums.count(nums[-1])

        if counter1 == 1 and counter2 == 1:
            return max(nums[0], nums[-1])
        if counter1 == 1:
            return nums[0]
        if counter2 == 1:
            return nums[-1]
        return -1
            
