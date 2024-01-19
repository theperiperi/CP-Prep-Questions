class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=list(ransomNote)
        s=list(magazine)
        for i in r:
            if i not in s:
                return False
            else:
                s=s.remove(i)
        return True
        
        
