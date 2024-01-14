class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq=list(set(nums))
        nums.clear()
        nums.extend(unq)
        nums.sort()
        return len(unq)
