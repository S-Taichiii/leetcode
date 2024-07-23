# class Node:
#     def __init__(self, data: int):
#         self.data: int = data
#         self.next = None
#
# class MinStack:
#     def __init__(self):
#         self.head = None
#         
#     def push(self, val: int) -> None:
#         tmp = self.head
#         self.head = Node(val)
#         self.head.next = tmp
#         
#     def pop(self) -> None:
#         if self.top() != None:
#             self.head = self.head.next
#
#     def top(self) -> int:
#         return self.head.data
#         
#     def getMin(self) -> int:
#         iterator = self.head
#         min = self.head.data
#         while iterator != None:
#             if iterator.data < min:
#                 min = iterator.data
#             iterator = iterator.next
#         
#         return min

# 2123ms
# Beats5.08%
# 21.08MB
# Beats7.54%

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_vals):
            if val < self.min_vals[-1]: self.min_vals.append(val)
            else: self.min_vals.append(self.min_vals[-1])
        else:
            self.min_vals.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_vals.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]

# 61ms
# Beats24.93%
# 20.55MB
# Beats33.15%

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print( minStack.getMin() )
minStack.pop();
print( minStack.top() )
print( minStack.getMin() )


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
