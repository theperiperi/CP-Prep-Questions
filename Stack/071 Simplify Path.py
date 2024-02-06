class Solution:
    def simplifyPath(self, path: str) -> str:
        path_elements=path.split("/")
        m=[]

        for i in path_elements:

            #if not empty and ., remove element
            if i==".." and len(m)>0:
                m.pop()
            
            #appending file names required
            elif i!="." and i!="" and i!="..":
                m.append(i)

        return "/"+"/".join(m)        
