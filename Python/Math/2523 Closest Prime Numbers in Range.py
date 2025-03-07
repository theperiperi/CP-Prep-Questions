class Solution:
    def closestPrimes(self, lower_bound: int, upper_bound: int) -> list[int]:

        is_prime = [True] * (upper_bound + 1)
        is_prime[0] = is_prime[1] = False

        for number in range(2, int(upper_bound ** 0.5) + 1):
            if is_prime[number]:
                for multiple in range(number * number, upper_bound + 1, number):
                    is_prime[multiple] = False

        prime_numbers = [num for num in range(lower_bound, upper_bound + 1) if is_prime[num]]

        if len(prime_numbers) < 2:
            return [-1, -1]

        smallest_gap = float('inf')
        closest_pair = [-1, -1]

        for i in range(1, len(prime_numbers)):
            current_gap = prime_numbers[i] - prime_numbers[i - 1]
            if current_gap < smallest_gap:
                smallest_gap = current_gap
                closest_pair = [prime_numbers[i - 1], prime_numbers[i]]

        return closest_pair
