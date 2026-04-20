from BStree import BTree ,AVLNode
class AVLNode (AVLNode):
    def __init__(self, item):
        super().__init__(item)
        self.height = 1

class AVLTree (BTree) :
    def __init__(self):
        super().__init__()
    
    def get_height(self,node : AVLNode) :
        if not node :
            return 0
        return node.height
    
    def get_balance(self, node) :
        balance_factor = self.get_height(node.left) - self.get_height(node.right)
        return balance_factor
    
    def right_rotation (self , node):
        y = node.left
        yr = y.right
        y.right = node 
        node.left = yr 
        node.height = 1+ max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+ max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def left_rotation(self,node):
        y = node.right
        yl = y.left
        y.left = node 
        node.right = yl 
        node.height = 1+ max(self.get_height(node.left),self.get_height(node.right))
        y.height = 1+ max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def insert(self, value):

        self.root = self._recursive_insertion(self.root , value)
    


    def _recursive_insertion (self , node , value):
        if not node :
            return AVLNode(value)
        if value < node.value :
            node.left = self._recursive_insertion(node.left , value)
        elif value > node.value :
            node.right = self._recursive_insertion(node.right , value)
        node.height = 1+ max(self.get_height(node.left),self.get_height(node.right))
        node_balance = self.get_balance(node)
        if node_balance >1 :
            if value < node.left.value :
                return self.right_rotation(node)
            elif value > node.left.value :
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
        if node_balance < -1 :
            if value > node.right.value:
                return self.left_rotation(node)
            elif value < node.right.value :
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
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
        node.height = 1+ max(self.get_height(node.left),self.get_height(node.right))
        node_balance = self.get_balance(node)
        if node_balance >1 :
            if  self.get_balance(node.left) >= 0:
                return self.right_rotation(node)
            else:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
        if node_balance < -1 :
            if self.get_balance(node.right) <= 0:
                return self.left_rotation(node)
            else :
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
        return node   