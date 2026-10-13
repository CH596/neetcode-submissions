class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.min_list.append(self.stack[0])
        elif val <= self.min_list[-1]:
            self.min_list.append(val)
        return
        

    def pop(self) -> None:
        if self.stack[-1] == self.min_list[-1]:
            self.min_list.pop(-1)
        self.stack.pop(-1)
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_list[-1]

        
