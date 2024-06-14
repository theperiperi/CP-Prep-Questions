class Solution:
    def isHappy(self, n: int) -> bool:
        lst=set()
        while(n!=1 and n not in lst):
            lst.add(n)
            n=sum(int(i)**2 for i in str(n))
        if n==1:
            return True
        return False
        
