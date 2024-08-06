#solved using counting, can also be done using hashmaps

class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = Counter(word)
        result = 0
        for ind, val in enumerate(sorted(frequency.values(), reverse=True)):
            result += (ind // 8 + 1) * val
        return result
