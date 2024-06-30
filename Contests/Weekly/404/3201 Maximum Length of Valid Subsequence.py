class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even=0
        odd=0
        even_odd=0
        odd_even=0

        for num in nums:
            if num%2==0:
                even+=1
                odd_even=even_odd+1
            else:
                odd+=1
                even_odd=odd_even+1
        return max(even,odd,odd_even,even_odd)
            



        
