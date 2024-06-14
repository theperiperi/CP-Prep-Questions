class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val=0
        for i,c in enumerate(reversed(columnTitle.upper())):
            val+=(26**i)*(ord(c)-ord("A")+1)
        return val
