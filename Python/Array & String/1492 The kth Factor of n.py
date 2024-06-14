class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans=[1]
        i=2
        count=1
        while count<k and i<=n:
            if n%i==0:
                ans.append(i)
                count+=1
            i+=1
        
        if len(ans)<k:
            return -1
        return ans[k-1]
            
