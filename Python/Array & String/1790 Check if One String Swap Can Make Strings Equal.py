class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff= 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
        return diff <=2 and sorted(s1)==sorted(s2)
