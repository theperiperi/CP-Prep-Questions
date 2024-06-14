class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        chars = set(words[0])

        for char in chars:
            frequency = min([word.count(char) for word in words])
            result += frequency * [char]
        return result
