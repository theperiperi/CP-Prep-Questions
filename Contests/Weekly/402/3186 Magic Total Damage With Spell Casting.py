class Solution:
    def maximumTotalDamage(self, powers: List[int]) -> int:
        damage_frequency = defaultdict(int)
        for power in powers:
            damage_frequency[power] += 1
        
        sorted_powers = sorted(damage_frequency.keys())
        
        n = len(sorted_powers)
        max_damage = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_damage = sorted_powers[i - 1] * damage_frequency[sorted_powers[i - 1]]
            take_damage = current_damage
            
            for j in range(i - 2, -1, -1):
                if sorted_powers[i - 1] - sorted_powers[j] > 2:
                    take_damage += max_damage[j + 1]
                    break
            
            dont_take_damage = max_damage[i - 1]
            max_damage[i] = max(take_damage, dont_take_damage)
        
        return max_damage[n]
