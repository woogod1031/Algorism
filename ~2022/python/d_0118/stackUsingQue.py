class MyStack(object):

    def __init__(self):
        self.input = collections.deque

    def push(self, x):
        self.input.append(x)
        
    def pop(self):
        if not self.input:
            return 
        else:
            return self.input.popleft()
    
    def top(self):
        return self.input[0]
        
    def empty(self):
        return self.input == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()