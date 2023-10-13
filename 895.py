class FreqStack:

    def __init__(self):
        self.freq = {}
        self.dictionary = defaultdict(list)
        self.max_freq = 0
    def push(self, val: int) -> None:
        if self.freq.get(val) == None:
            self.freq[val] = 1
        else:
            self.freq[val] = self.freq[val] + 1
        self.dictionary[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.dictionary[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.dictionary[self.max_freq]) == 0:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()