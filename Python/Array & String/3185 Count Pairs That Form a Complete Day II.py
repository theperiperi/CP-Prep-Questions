class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = defaultdict(int)
        count = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            if complement in remainder_count:
                count += remainder_count[complement]
            remainder_count[remainder] += 1
        
        return count
