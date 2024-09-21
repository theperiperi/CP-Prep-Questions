class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_list = []
        current_number = 1

        for _ in range(n):
            lexicographical_list.append(current_number)
            current_number = self.get_next_lexical_number(current_number, n)

        return lexicographical_list

    def get_next_lexical_number(self, current_number: int, n: int) -> int:
        if current_number * 10 <= n:
            return current_number * 10

        if current_number >= n:
            current_number //= 10

        current_number += 1
        
        while current_number % 10 == 0:
            current_number //= 10

        return current_number
