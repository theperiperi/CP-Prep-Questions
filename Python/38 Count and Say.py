class Solution:
    def countAndSay(self, n: int) -> str:
        res ='1'
        for _ in range(1,n):
            res = self.build_next(res)
        return res
    
    def build_next(self,s:str)->str:
        result =''
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                result+= str(count) +s[i-1]
                count = 1
        result+= str(count) + s[-1]
        return result
