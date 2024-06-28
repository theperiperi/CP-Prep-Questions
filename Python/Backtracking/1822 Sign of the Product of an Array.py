class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign=1
        for num in nums:
            print(num)
            if num==0:
                return 0
            if num<0:
                if sign==1:
                    sign=-1
                else:
                    sign=1
                
        return sign
        
