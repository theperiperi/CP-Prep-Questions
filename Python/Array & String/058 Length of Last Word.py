class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        s=s.split(" ")
        a=list(s)
        return len(a[-1])
