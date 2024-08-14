class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def countPairsWithMaxDistance(maxDistance):
            pairCount = 0
            leftIndex = 0
            for rightIndex in range(len(nums)):
                while nums[rightIndex] - nums[leftIndex] > maxDistance:
                    leftIndex += 1
                pairCount += rightIndex - leftIndex
            return pairCount
        
        minDistance, maxDistance = 0, nums[-1] - nums[0]
        
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            if countPairsWithMaxDistance(midDistance) >= k:
                maxDistance = midDistance
            else:
                minDistance = midDistance + 1
        
        return minDistance
