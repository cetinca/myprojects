class MinStack:

    def __init__(self):
        self.stack = [(None, float("inf"))]

    def push(self, val: int) -> None:
        s = self.stack[-1]
        self.stack.append((val, min(val, s[1])))

    def pop(self) -> None:
        e = self.stack.pop()
        return e[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



m = MinStack()

m.push(5)
m.push(3)

print(m.stack)
print(m.getMin())
print(m.top())