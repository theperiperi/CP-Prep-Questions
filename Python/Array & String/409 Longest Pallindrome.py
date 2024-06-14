class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=defaultdict(int)
        length=0
        middle_bit=0
        for i in s:
            dic[i]+=1
        for i in dic.keys():
            while dic[i]>=2:
                length+=2
                dic[i]-=2
            if dic[i]>0:
                middle_bit=1
        if middle_bit==1:
            length+=1
        return length
