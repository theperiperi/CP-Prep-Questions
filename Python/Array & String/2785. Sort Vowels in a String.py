class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = set("AEIOUaeiou")
        vowels = [c for c in s if c in vowels_set]
        vowels.sort()

        result = []
        ptr = 0

        for c in s:
            if c in vowels_set:
                result.append(vowels[ptr])
                ptr += 1
            else:
                result.append(c)

        return ''.join(result)
