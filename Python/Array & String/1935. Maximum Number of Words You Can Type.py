class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        # count = 0
        # for ch in text.split():
        #     if all(c not in brokenLetters for c in ch):
        #         count += 1
        # return count
        count = 0
        words=text.split()
        for ch in words:
            found = True
            for c in brokenLetters:
                if c in ch:
                    found = False
                    break
            if found:
                count += 1
        return count
