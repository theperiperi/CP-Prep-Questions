class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashy=defaultdict(int)
        for i in arr:
            hashy[i]+=1
        return len(hashy.values())==len(set(hashy.values()))
