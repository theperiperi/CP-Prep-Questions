class ProductOfNumbers:
    def __init__(self):
        self.arr = [1]
        self.last_idx = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
            self.last_idx = len(self.arr) - 1
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        size = len(self.arr)
        if size - k - 1 < self.last_idx:
            return 0
        return self.arr[-1] // self.arr[size - k - 1]
