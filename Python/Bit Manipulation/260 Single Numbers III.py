class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0

        #xor all the numbers a^a cancels out
        for num in nums:
            xor=xor^num
        
        #set rightmost bit
        mask=xor&-xor

        num1=num2=0
        #partition number into 2 groups and xor each
        for num in nums:
            if num &mask:
                num1=num1^num
            else:
                num2=num2^num
        return [num1,num2]
