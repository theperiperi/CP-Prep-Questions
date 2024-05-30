class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        memo=set()
        for num in nums:
            if num in memo:
                #repeated number
                #sum of n natural numbers-actual sum+num considered
                return [num,(n*(n+1)//2)-sum(nums)+num]
            memo.add(num)
