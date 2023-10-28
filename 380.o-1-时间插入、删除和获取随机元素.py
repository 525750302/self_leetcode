import random
class RandomizedSet:

    def __init__(self):
        self.data_set = set()
        self.stack = []

    def insert(self, val: int) -> bool:
        last = len(self.data_set)
        self.data_set.add(val)
        if last != len(self.data_set):
            self.stack.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        last = len(self.data_set)
        self.data_set.discard(val)
        if last != len(self.data_set):
            self.stack.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        random_result = int(random.random() * len(self.stack))
        return self.stack[random_result]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()