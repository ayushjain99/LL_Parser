class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self,item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def top(self):
    	return self.stack[-1]

    def print_bottom_up(self):
    	str = ''
    	for i in self.stack:
    		str = str + i
    	return str
