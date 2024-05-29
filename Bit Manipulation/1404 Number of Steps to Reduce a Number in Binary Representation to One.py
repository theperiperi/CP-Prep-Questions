class Solution:
    def numSteps(self, s: str) -> int:
        value=int(s,2)
        i=0
        while value!=1:
            if value%2==0:
                value//=2
            else:
                value+=1
            i+=1
        return i
