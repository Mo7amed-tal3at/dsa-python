class Heap :
    def __init__(self , arr = None):
        self.heap = [] if not arr else arr
        if arr:
            self._heapify()
    
    
    @property
    def size (self):
        return len(self.heap)
    
    def _swap(self , i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def _bubble_up (self,index) :
        if index == 0 :
            return index
        parent = (index -1) // 2
        if self.heap[index] > self.heap[parent] :
            self._swap(index,parent)
            return self._bubble_up(parent)
        else :
            return index

    def insert(self, value) :
        self.heap.append(value)
        self._bubble_up(self.size-1)


    def _bubble_down (self, index , size = None):
        size = size if size else self.size
        left_child = 2* index +1
        right_child = 2* index +2
        if left_child >= size :
            return index
        else :
            largest = left_child
            if right_child < size and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if self.heap[index] < self.heap[largest]:
                self._swap(index, largest)
                return self._bubble_down(largest, size)

            return index

    def get_max(self):
        if not self.heap :
            raise Exception("Heap is empty")
        return self.heap[0]
    
    def extract_max(self):
        if not self.heap:
            raise Exception("Heap is empty")
        self._swap(0,self.size -1)
        maximum = self.heap.pop()
        self._bubble_down(0)
        return maximum
    
    def _heapify (self):
        for i in range((self.size//2)-1 , -1 ,-1) :
            self._bubble_down(i)

    def heap_sort(self):
        if not self.heap :
            raise Exception("Pass Array")
        count = self.size-1
        while count > 0:
            self._swap(0,count)
            self._bubble_down(0,count)
            count -= 1
        return self.heap