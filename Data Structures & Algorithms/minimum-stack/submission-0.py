class MinStack:

    def __init__(self):
        self.min_stack, self.stack = [], []
        
    def push(self, value: int) -> None:
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
