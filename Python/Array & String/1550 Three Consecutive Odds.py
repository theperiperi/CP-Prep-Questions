class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        max_count=0
        count=0
        for num in arr:
            if num%2==1:
                count+=1
            else:
                count=0
            max_count=max(max_count,count)
        
        if max_count>=3:
            return True
        return False
