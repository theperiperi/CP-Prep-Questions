class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        start=0
        curr_cost=0
        max_length=0

        for end in range(n):
            curr_cost+=abs(ord(s[end])-ord(t[end]))
            
            while curr_cost>maxCost:
                curr_cost-=abs(ord(s[start])-ord(t[start]))
                start+=1
            
            max_length=max(max_length,end-start+1)
        return max_length
