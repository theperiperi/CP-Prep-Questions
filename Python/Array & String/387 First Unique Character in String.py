class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i,j in count.items():
            if j==1: # checking if occurence is 1
                return s.index(i)
        return -1
