class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = [-math.inf] * len(energy)
        for i in range(len(energy)):
            if i - k >= 0:
                res[i] = max(res[i-k] + energy[i], energy[i])
            else:
                res[i] = energy[i]

        return max(res[len(energy)-k:])
      
