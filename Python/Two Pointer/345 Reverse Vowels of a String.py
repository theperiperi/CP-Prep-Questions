class Solution:
    def reverseVowels(self, s: str) -> str:
        start=0
        end=len(s)-1
        vowels="aeiouAEIOU"
        s=list(s)
        while start<end:
            if s[start] in vowels and s[end] in vowels:
                s[start],s[end]=s[end],s[start]
                end-=1
            elif s[start] in vowels and s[end] not in vowels:
                end-=1
                continue
            start+=1
        return "".join(s)
