class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count=0
        diff=0
        for index,value in enumerate(arr):
            diff+=value-index
            if diff==0:
                count+=1
        return count
