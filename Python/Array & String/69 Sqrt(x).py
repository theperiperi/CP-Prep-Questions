#newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        b = x
        while b*b > x: 
            b=(b+x//b)//2
        return b
