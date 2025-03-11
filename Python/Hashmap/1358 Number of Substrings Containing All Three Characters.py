class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        dictionary = {"a": 0, "b": 0, "c": 0}

        for right in range(len(s)):
            dictionary[s[right]] += 1

            while dictionary['a'] > 0 and dictionary["b"] > 0 and dictionary["c"]>0:
                count += len(s) - right
                dictionary[s[left]] -= 1
                left += 1
        
        return count
