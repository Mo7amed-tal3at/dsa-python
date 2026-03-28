class Node :
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList :
    def __init__(self, head = None):
            
            self.head = head
            self.last = head
            self.len  = 1 if head else 0
    def insert(self, val):
        newNode = Node(val)
        if self.len == 0 :
             self.head = self.last = newNode
             self.len =1
        else :
             self.last.next = newNode
             self.last = newNode
             self.len +=1
    def delete_first(self):
        if self.len == 0:
             raise Exception("Linked List is Empty")
        self.head = self.head.next
        self.len -=1
        if self.len ==0:
             self.last = None
     
    def delete_last(self):
        if self.len == 0:
             raise Exception("Linked List is Empty")
        elif self.len > 1 :
            current = self.head
            while current.next != self.last:
                current= current.next
            self.last = current 
            self.last.next = None
            self.len -=1
        else :
            self.head = self.last =None
            self.len = 0
        
    def delete_at_position(self, position: int):
         if position < 1 or position > self.len :
              raise Exception("Position Out Of LinkedList Index")
         elif position == 1:
              self.delete_first()
         elif position == self.len :
              self.delete_last()
         else :
              current = self.head 
              current_position =1 
              while current_position< position-1 :
                   current= current.next
                   current_position +=1
              current.next = current.next.next
              self.len -=1
    
    def display(self):
         print(self.len)
         current = self.head
         result = ""
         while current :
              result += f"{current.val} -> "
              current=current.next
         print(result + "None")