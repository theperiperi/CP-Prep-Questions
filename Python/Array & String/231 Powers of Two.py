class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return 0
        while n!=1:
            if n%2:
                return False
            else:
                n//=2
        return True
        
