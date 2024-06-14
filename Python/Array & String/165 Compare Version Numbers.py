class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        # Convert version parts to integers for proper comparison
        v1 = [int(ele) for ele in v1]
        v2 = [int(ele) for ele in v2]

        i=0
        while i<min(len(v1),len(v2)):
            if v1[i]>v2[i]:
                return 1
            if v1[i]<v2[i]:
                return -1
            #if equal
            i+=1
        
        while v1[-1]==0:
            v1.pop()
        while v2[-1]==0:
            v2.pop()
        if len(v1)==len(v2):
            return 0
        if len(v1)>len(v2):
            return 1
        return -1
        

