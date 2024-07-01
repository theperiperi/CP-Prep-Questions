class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust:
            return 1
        
        trust_counts=[0]*(n+1)
        trust_others=[0]*(n+1)

        for start,end in trust:
            trust_counts[end]+=1
            trust_others[start]+=1
        
        for person in range(1,n+1):
            if trust_counts[person]==n-1 and trust_others[person]==0:
                return person
        return -1
