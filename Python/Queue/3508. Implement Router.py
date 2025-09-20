from collections import deque,defaultdict
import bisect
class Router(object):
    def __init__(self,memoryLimit):
        self.q=deque()
        self.m=memoryLimit
        self.used_pac=set()
        self.l=0
        self.dest_map=defaultdict(list)
    def addPacket(self,s,d,t):
        temp_p=(s,d,t)
        if temp_p in self.used_pac:
            return False
        if self.l>=self.m:
            old=self.q.popleft()
            self.used_pac.remove(old)
            self.dest_map[old[1]].pop(0)
            self.l-=1
        self.q.append(temp_p)
        self.used_pac.add(temp_p)
        self.dest_map[d].append(t)
        self.l+=1
        return True
    def forwardPacket(self):
        if self.l==0:
            return []
        self.l-=1
        p=self.q.popleft()
        self.used_pac.remove(p)
        self.dest_map[p[1]].pop(0)
        return list(p)
    def getCount(self,d,s,e):
        a=self.dest_map[d]
        return bisect.bisect_right(a,e)-bisect.bisect_left(a,s)
