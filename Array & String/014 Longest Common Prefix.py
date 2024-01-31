class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substr=""

        for i in zip(*strs):
            if len(set(i))==1:
                substr+=i[0]
            else:
                return substr
        return substr



        

        
