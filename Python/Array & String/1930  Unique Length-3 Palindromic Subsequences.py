class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for character in set(s):
            first = s.find(character)
            last = s.rfind(character)
            if first != last:
                ans += len(set(s[first+1:last]))
        return ans
