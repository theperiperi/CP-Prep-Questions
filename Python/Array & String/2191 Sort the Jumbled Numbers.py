class Solution:
    def sortJumbled(self, mapping, nums):
        numsSize = len(nums)
        mappedAndIndexPairs = []  

        for i in range(numsSize):
            originalNum = nums[i]
            mappedNum = mapping[0] if originalNum == 0 else 0  
            placeValue = 1  

            while originalNum > 0:
                digit = originalNum % 10 
                mappedNum += placeValue * mapping[digit] 
                originalNum //= 10  
                placeValue *= 10  

            mappedAndIndexPairs.append((mappedNum, i))

        mappedAndIndexPairs.sort()
        sortedNums = [nums[i] for _, i in mappedAndIndexPairs]
        return sortedNums
