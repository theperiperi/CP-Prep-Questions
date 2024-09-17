class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        d=dict()

        for i in nums:
            if(i in d.keys()):
                d[i]+=1
            else:
                d[i]=1
            if(d[i]==2):
                l.append(i)
        return(l)    
