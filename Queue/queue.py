class Node :
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue :
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self,value):
        new_node = Node(value)
        if self.size ==0:
            self.front = self.back = new_node
        
        else:
            self.back.next = new_node
            self.back = new_node
        self.size +=1

    def dequeue (self ):
        if not self.front :
            raise Exception("Queue is Empty")
        returned_node = self.front 
        self.front = self.front.next 
        if not self.front :
            self.back = None
        self.size -=1
        return returned_node
        
    def peek(self):
        if not self.front :
            raise Exception("Queue is Empty")
        return self.front.value
    
    def is_empty(self):
        return self.front is None
    
    def __len__(self):
        return self.size