"""

A stack is fundementally the opposite of a queue. 
Envision a stack of blocks, where you keep on adding blocks (elements) higher and higher.
The first block to leave will be the top block.
But wait!
The top block was actually the last one in.
Therefore, a stack is based around "Last in, first out."

"""

class stack:
    def __init__(self):
        self.items = []
    def leave(self):
        popvar = self.items[-1] # Yes, .pop() exists but I'd like to show the inner workings a bit
        del self.items[-1]
        return popvar
    def enter(self, item):
        self.items.append(item)

# Usage
x = stack()
x.enter(5)
x.enter(6)
print(x.items)
x.leave()
print(x.items)