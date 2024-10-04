class Solution:
    def numDecodings(self, encoded_string: str) -> int:
        if not encoded_string or encoded_string[0] == '0':
            return 0

        string_length = len(encoded_string)
        decode_ways = [0] * (string_length + 1)
        decode_ways[0] = 1
        decode_ways[1] = 1

        for i in range(2, string_length + 1):
            current_digit = int(encoded_string[i - 1])
            previous_two_digits = int(encoded_string[i - 2:i])

            if current_digit != 0:
                decode_ways[i] += decode_ways[i - 1]

            if 10 <= previous_two_digits <= 26:
                decode_ways[i] += decode_ways[i - 2]

        return decode_ways[string_length]
