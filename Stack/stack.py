class Node:

    def __init__(self, data) :
        self.data = data
        self.next: "Node | None" = None

class Stack:
    def __init__(self):
        self.top = None
        self.len = 0
    def push(self,data):
            newtop = Node(data)
            newtop.next = self.top
            self.top = newtop
            self.len += 1
    def pop(self):
        if not self.top:
            raise Exception("Can't pop empty stack")
        pop=self.top
        self.top = self.top.next
        self.len -=1
        return pop.data
    def peek(self):
        if not self.top:
            raise Exception("stack has no elements")

        return self.top.data
    def is_empty(self):
        return self.top is None
    def size(self):
        return self.len
    def __repr__(self):
        elements = []
        current = self.top
        while current :
            elements.append(str(current.data))
            current= current.next
        return "Top -> ["+", ".join(elements)+"]<- Bottom"    

