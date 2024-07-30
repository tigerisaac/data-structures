"""

A queeue is one of the basic structures of programming.
Think of people in line, waiting for the person in front of them to move forward or exit the line.
That's exactly what a queue is!
The principle of a queue is "First in, first out."
I'll keep the functions of the queue very high-level for ease of reading.

"""

class queue:
    def __init__(self):
        self.items = []
    def leave(self):
        popvar = self.items[-1] # Yes, .pop() exists but I'd like to show the inner workings a bit
        del self.items[-1]
        return  popvar
    def enter(self, item):
        self.items.insert(0, item) # Feels like cheating, if I feel like it I'll create a separate .insert() function to show how it works

# Usage
x = queue()
x.enter(5)
x.enter(6)
print(x.items)
x.leave()
print(x.items)