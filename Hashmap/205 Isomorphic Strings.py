class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1=[]
        map2=[]
        for i in range(len(s)):
            map1.append(s.index(s[i]))
            map2.append(t.index(t[i]))
        return map1==map2
        
        
        
