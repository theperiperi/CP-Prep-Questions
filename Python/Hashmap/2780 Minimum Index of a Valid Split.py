class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        freq = Counter(nums)
        dominant, total_count = max(freq.items(), key=lambda x: x[1])
        
        left_count = 0 
        
        for i, num in enumerate(nums):
            if num == dominant:
                left_count += 1 
                total_count -= 1
            
            if left_count > (i + 1) // 2 and total_count > (len(nums) - (i + 1)) // 2:
                return i
        
        return -1
