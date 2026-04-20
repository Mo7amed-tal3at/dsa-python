from Queue.queue import Queue

class Node :
    def __init__(self,item):
        self.left = None
        self.right = None
        self.value = item

class BTree :
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root :
            self.root = Node(value)
        else :
            self._recursive_insertion(self.root , value)
        

    def _recursive_insertion (self , node , value):
        if value < node.value :
            if node.left :
                self._recursive_insertion(node.left , value)
            else :
                node.left = Node(value)
        if value > node.value :
            if node.right :
                self._recursive_insertion(node.right , value)
            else :
                node.right = Node(value)
        return
    
    def search (self,value):
            return self._recursive_search(self.root , value)
    
    def _recursive_search (self , node , value):
        if value == node.value :
            return node 
        else :
            if value < node.value :
                if node.left :
                   return self._recursive_search(node.left , value)
                else :
                    raise Exception( "Not Found")
            if value > node.value :
                if node.right :
                    return self._recursive_search(node.right , value)
                else :
                    raise Exception( "Not Found")
        
    def display_inorder(self):
        self._recursive_display(self.root)
    def _recursive_display(self,node):
        if node :
            self._recursive_display(node.left)
            print(node.value)
            self._recursive_display(node.right)
    
    def display_level_order(self):
        lo_queue = Queue()
        lo_queue.enqueue(self.root)
        while not lo_queue.is_empty() :
            popped_node = lo_queue.dequeue()
            print(popped_node.value)
            if popped_node.left :
                lo_queue.enqueue(popped_node.left)
            if popped_node.right :
                lo_queue.enqueue(popped_node.right)

    def height(self):
        return self._recursive_height(self.root)

    def _recursive_height(self, node):
        if not node:
            return 0
        return 1 + max(self._recursive_height(node.left),self._recursive_height(node.right) )
    
    def get_successor(self,node):
        if node.left:
            return self.get_successor(node.left)
        else:
            return node
    
    def delete(self, value):
        self.root = self._recursive_delete(self.root, value)

    def _recursive_delete(self, node, value):
        if not node:
            raise Exception("Not Found")
        if value < node.value:
            node.left = self._recursive_delete(node.left, value)
        elif value > node.value:
            node.right = self._recursive_delete(node.right, value)
        else:  
            if not node.left and not node.right :
                return None
            elif not node.left :
                return node.right
            elif not node.right :
                return node.left
            else :
                successor = self.get_successor(node.right)
                node.value  = successor.value
                node.right=self._recursive_delete(node.right,successor.value)

        return node         
