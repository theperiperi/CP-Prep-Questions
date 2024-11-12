class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maxnum=float('inf')
        res=[[0,0,maxnum]]

        items.sort(key=lambda x:x[0])

        for price,beauty in items:
            lastBracket =res[-1]
            if beauty >lastBracket[1]:
                res[-1][2]=price
                res.append([price,beauty,maxnum])
        
        ans=[]

        for x in queries:
            for i in range(len(res)-1,-1,-1):
                if res[i][0]<=x:
                    ans.append(res[i][1])
                    break
        
        return ans
