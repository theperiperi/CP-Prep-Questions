class Solution:
    def numberOfPermutations(self, n, requirements):
        MODULO = 10**9 + 7
        MAX_INVERSIONS = 400
        
        inversion_requirements = {req[0] + 1: req[1] for req in requirements}
        
        dp = [[0] * (MAX_INVERSIONS + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for length in range(1, n + 1):
            for current_inversion in range(MAX_INVERSIONS + 1):
                dp[length][current_inversion] = sum(dp[length - 1][current_inversion - new_pos]
                                                    for new_pos in range(length)
                                                    if current_inversion - new_pos >= 0) % MODULO
            
            if length in inversion_requirements:
                target_inversion = inversion_requirements[length]
                dp[length] = [0 if inv != target_inversion else dp[length][inv] for inv in range(MAX_INVERSIONS + 1)]
        
        total_permutations_with_required_inversions = sum(dp[n]) % MODULO
        
        return total_permutations_with_required_inversions
