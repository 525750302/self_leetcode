
class MinStack:

    def __init__(self):
        self.stack = []
        self.point = None
        self.point_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.point == None:
            self.point = val
            self.point_stack.append(val)
        elif self.point <= val:
            self.point_stack.append(self.point)
        else:
            self.point_stack.append(val)
            self.point = val

    def pop(self) -> None:
        self.stack.pop()
        self.point_stack.pop()
        if len(self.point_stack) > 0:
            self.point = self.point_stack[-1]
        else:
            self.point = None


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.point_stack[-1]
    



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()