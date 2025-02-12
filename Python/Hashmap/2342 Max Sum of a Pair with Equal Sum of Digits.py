class Solution:
    def get_digits_sum(self, number) -> int:
        digits_sum = 0
    
        while number > 0:
            digits_sum += number % 10
            number //= 10

        return digits_sum

    def maximumSum(self, nums: List[int]) -> int:
        numbers = nums

        digits_sum_map = {}

        for number in numbers:
            digits_sum = self.get_digits_sum(number=number)

            if digits_sum not in digits_sum_map:
                digits_sum_map[digits_sum] = []
            
            digits_sum_map[digits_sum].append(number)

        maxium_sum_of_same_digits_sum = 0

        for numbers in digits_sum_map.values():
            numbers_length = len(numbers)

            numbers.sort()

            if numbers_length < 2:
                continue
            
            last_number, penultimate_number = numbers[-1], numbers[-2]
            maxium_sum_of_same_digits_sum = max(maxium_sum_of_same_digits_sum, last_number + penultimate_number)
        
        if maxium_sum_of_same_digits_sum == 0:
            return -1

        return maxium_sum_of_same_digits_sum
