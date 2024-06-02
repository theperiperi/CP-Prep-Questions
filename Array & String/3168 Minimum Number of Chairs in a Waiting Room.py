class Solution:
    def minimumChairs(self, s: str) -> int:
        m=0
        count=0
        for i in s:
            if i=="E":
                count+=1
            if i=="L":
                count-=1
            m=max(m,count)
        return m
