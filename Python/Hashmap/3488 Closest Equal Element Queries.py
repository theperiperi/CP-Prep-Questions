class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        value_indices = defaultdict(list)

        # Store indices of each unique number in nums
        for index, value in enumerate(nums):
            value_indices[value].append(index)

        # Process each group of indices for the same value
        for indices in value_indices.values():
            size = len(indices)
            if size == 1:  # If there's only one occurrence, mark it as -1
                nums[indices[0]] = -1
                continue
            
            # Compute the minimum circular distance for each index
            for i in range(size):
                next_index = indices[(i + 1) % size]
                prev_index = indices[(i - 1 + size) % size]

                forward_dist = min((n - indices[i] - 1) + next_index + 1, abs(indices[i] - next_index))
                backward_dist = min(abs(prev_index - indices[i]), indices[i] + (n - prev_index))

                nums[indices[i]] = min(forward_dist, backward_dist)

        # Map the query results
        return [nums[q] for q in queries]
