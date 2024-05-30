class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half=len(s)//2
        a=s[:half]
        b=s[half:]
        vowels="aeiouAEIOU"
        vowa=0
        vowb=0

        for i in range(half):
            if a[i] in vowels:
                vowa+=1
            if b[i] in vowels:
                vowb+=1
        return vowa==vowb
