class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        size = len(pref)
        count=0
        for word in words:
            if word[:size]==pref:
                count+=1
        return count
