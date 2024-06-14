class RandomizedSet:

    def __init__(self):
        self.val_and_index = {}
        self.lst = []
        
    def insert(self, val: int) -> bool:
        if val not in self.val_and_index:
            self.lst.append(val)
            self.val_and_index[val] = len(self.lst) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_and_index:
            index = self.val_and_index[val]
            last_val = self.lst[-1]

            # Swap the value at index with the last value in the list
            self.lst[index] = last_val
            self.val_and_index[last_val] = index

            # Remove the value from the dictionary and the list
            del self.val_and_index[val]
            self.lst.pop()

            return True
        return False

    def getRandom(self) -> int:
        import random
        return random.choice(self.lst)
