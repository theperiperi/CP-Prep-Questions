class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length_pattern=len(p)
        length_str=len(s)

        i=0
        t=0

        i_index=-1 # Index of '*' in pattern
        t_index=-1 # Index in string where we started matching after encountering '*'

        while t<length_str:
            if i<length_pattern and (p[i]==s[t] or p[i]=="?"):
                i+=1
                t+=1
            elif i<length_pattern and p[i]=="*":
                #saving index of *
                i_index=i
                t_index=t
                i+=1

            #if * encountered
            elif i_index!=-1:
                i=i_index+1 #start matching from the char after "*"
                t_index+=1  #move to next char
                t=t_index
            else:
                return False
        
        while i<length_pattern and p[i]=="*":
            i+=1
        
        return i==length_pattern
