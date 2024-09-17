class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        max_score_stage0 = max_score_stage1 = max_score_stage2 = max_score_stage3 = -float('inf')
        multiplier_0, multiplier_1, multiplier_2, multiplier_3 = a

        for element_b in b:
            max_score_stage3 = max(max_score_stage3, max_score_stage2 + multiplier_3 * element_b)
            max_score_stage2 = max(max_score_stage2, max_score_stage1 + multiplier_2 * element_b)
            max_score_stage1 = max(max_score_stage1, max_score_stage0 + multiplier_1 * element_b)
            max_score_stage0 = max(max_score_stage0, multiplier_0 * element_b)
    
        return max_score_stage3
