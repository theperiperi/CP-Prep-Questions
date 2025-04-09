class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for num in set(nums):
            if num>k:
                count+=1
            elif num<k:
                return -1
        return count
