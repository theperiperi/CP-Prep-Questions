class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """

        characters = list(word)
        seen_chars = set()
        if len(characters) < 4:
            return 0

        length = len(characters)
        start = 0
        end = 3
        count = 0
        seen_chars.add(characters[0])

        while end < length:
            if characters[end] in seen_chars:
                count += 1
                start = end + 1
                end = start + 3
                if start < length:
                    seen_chars = set(characters[start])
            else:
                seen_chars.add(characters[end - 2])
                end += 1

        return count
