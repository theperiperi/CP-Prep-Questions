class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)

        for i in range(1, n+1):
            count=0
            for num in nums:
                if num>=i:
                    count+=1
            if count==i:
                return count
        return -1
