class Solution:
    def canJump(self, nums: List[int]) -> bool:
        initial=0
        for i in nums:
            if initial<0:
                return False
            if i>initial:
                initial=i
            initial-=1  

        return True
