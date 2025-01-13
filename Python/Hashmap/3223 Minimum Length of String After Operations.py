class Solution:

    def minimumLength(self, s: str) -> int:
        char_Set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        ans = 0
        for ch in char_Set:
            count = s.count(ch)
            if count & 1:
                ans += 1
            elif count != 0:
                ans += 2
        return ans
