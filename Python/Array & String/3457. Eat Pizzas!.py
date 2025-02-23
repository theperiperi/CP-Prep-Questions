class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        day_count = len(pizzas) // 4
        even_count = day_count // 2
        odd_count = day_count - even_count

        pizzas.sort(reverse = True)
        index = 0
        weight = 0 

        for i in range(odd_count):
            weight += pizzas[index]
            index += 1

        index += 1
        
        for i in range(even_count):
            weight += pizzas[index]
            index +=2

        return weight
