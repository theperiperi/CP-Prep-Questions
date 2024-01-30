class RandomizedSet:

    def __init__(self):
        self.st=set()
        

    def insert(self, val: int) -> bool:
        if val not in self.st:
            self.st.add(val)
            return True
        return False        

    def remove(self, val: int) -> bool:
        if val in self.st:
            self.st.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        import random
        ind=random.randint(0, len(self.st)-1)
        lst=list(self.st)
        return lst[ind]
        


# Your RandomizedSet object will be inself.stantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
