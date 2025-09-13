class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        maxVowel, maxConso = 0, 0
        for char in s:
            i = ord(char) - ord('a')
            freq[i] += 1
            if char in 'aeiou':
                maxVowel = max(maxVowel, freq[i])
            else:
                maxConso = max(maxConso, freq[i])
        return maxVowel + maxConso
