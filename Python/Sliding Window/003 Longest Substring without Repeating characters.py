class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1=set()
        max_length=0
        left_pointer=0
        right_pointer=0
        hashmap=defaultdict(int)
        length=0

        while right_pointer!=len(s):
            if s[right_pointer] not in hashmap:
                length+=1

            else:
                left_pointer=hashmap[s[right_pointer]]+1
                right_pointer=left_pointer
                hashmap.clear()
                length=1

            #letter and index it occurs at
            hashmap[s[right_pointer]]=right_pointer
            max_length=max(max_length,length)
            right_pointer+=1
        print(hashmap)
        return max_length
        


        
