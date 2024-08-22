class Solution:
    def findComplement(self, num: int) -> int:
        s = ""
        for i in bin(num)[2:]:
            if i =="0":
                s+="1"
            else :s+="0"
        return int(s,2)
