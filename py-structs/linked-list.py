"""

Linked lists don't exactly find a place in Python, as you don't have to manage every little detail about your memory.
However, I'll add an implementation here, just for ease of understanding.
A more in-depth explanation can be found in the c-structs file.

"""

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None # Initialize the node

class LList:
    
    def __init__(self):
        self.head = None
    
    def insert_first(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node # Set this node as the head
            return
        else:
            new_node.next = self.head # Set this node's next to the current head
            self.head = new_node # Set the current head to the new node
    
    def insert_index(self, item, index):
        new_node = Node(item)
        if index == 0:
            self.insert_first(item)
        pos = 0 # You can only move linearly throughout a linked list
        current_node = self.head
        while (current_node != None and pos + 1 != index):
            current_node = current_node.next
            pos += 1
        if current_node == None:
            print("Index out of range")
            return
        else:
            new_node.next = current_node.next # Replace current node basically
            current_node.next = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node  # Add the new node to the end
    
    def upd_nodeitem(self, item, index):
        current_node = self.head
        pos = 0
        if index == pos:
            current_node.item = item # Upd item
        else:
            while (current_node.head != None and pos != index): # Find index
                current_node = current_node.next
                pos += 1
            if current_node.head == None:
                print("Index out of range")
                return
            else:
                current_node.item = item # Upd item
    
    def rem_firstnode(self):
        if self.head == None:
            return
        
        self.head = self.head.next
    
    def rem_lastnode(self):
        current_node = self.head
        while (current_node.next != None and current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None

    def rem_indexnode(self, index):
        current_node = self.head
        pos = 0
        if index == pos:
            self.rem_firstnode
        while (current_node != None and pos + 1 != index):
            current_node = current_node.next
            pos += 1
        if current_node == None:
            print("Index out of range")
            return
        else:
            current_node.next = current_node.next.next
    
    def get_size(self):
        count = 1
        current_node = self.head
        while (current_node.head != None):
            current_node = current_node.next
            count += 1

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.item)
            current_node = current_node.next

# USAGE
llist = LList()

llist.insert_end('a')
llist.insert_end('b')
llist.insert_first('c')
llist.insert_end('d')
llist.insert_index('g', 2)

llist.printLL()

print("\nRemove First Node")
llist.rem_firstnode()
print("Remove Last Node")
llist.rem_lastnode()
print("Remove Node at Index 1")
llist.rem_indexnode(1)

llist.printLL()