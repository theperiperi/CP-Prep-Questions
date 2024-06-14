from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_hashmap = defaultdict(int)
        left_pointer = 0
        result = 0
        max_count = 0

        for right_pointer in range(len(s)):
            count_hashmap[s[right_pointer]] += 1
            max_count = max(max_count, count_hashmap[s[right_pointer]])
            window_length = right_pointer - left_pointer + 1

            if window_length - max_count > k:
                count_hashmap[s[left_pointer]] -= 1
                left_pointer += 1

            result = max(result, right_pointer - left_pointer + 1)

        return result
