class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount=defaultdict(int)
        tcount=defaultdict(int)
        for i in range(len(s)):
            scount[s[i]]+=1
            tcount[t[i]]+=1
        print(scount,tcount)
        for i in scount.keys():
            if i in tcount.keys():
                tcount[i]-=scount[i]
                if tcount[i]<0:
                    tcount[i]=0
        return sum(tcount.values())
