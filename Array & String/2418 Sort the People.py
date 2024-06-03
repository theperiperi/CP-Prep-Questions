class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = []
        for i in range(len(names)):
            x.append([heights[i],names[i]]) 
        x.sort(reverse = True)
        y = []
        for i in range(len(names)):
            y.append(x[i][1])
        return y
        
