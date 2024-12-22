class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
      
        nums.sort()
        
        # To track the last used distinct value
        last_used = float('-inf')
        distinct_count = 0
        
        for num in nums:
            # Start of the range
            start = max(num - k, last_used + 1)
            
            if start <= num + k:
                # Assign the smallest valid distinct value
                last_used = start
                distinct_count += 1
        
        return distinct_count

