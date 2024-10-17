class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_index = {int(digits[i]) : i for i in range(len(digits))}

        for i in range(len(digits)):
            curr_digit = int(digits[i])
            for d in range(9, curr_digit, -1):
                if last_index.get(d, -1) > i:
                    digits[i], digits[last_index[d]] = digits[last_index[d]], digits[i]
                    return int(''.join(digits))

        return num
