class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = []
        vowels = ['a','e','i','o','u']

        for vowel in vowels:
            if(vowel in s):
                return True
        return False
