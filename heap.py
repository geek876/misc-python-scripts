class Heap:

    def __init__(self, array):
        self._heap =  array

    def get_heap(self):
        return self._heap

    def get_left_child(self,parent):
        _parent_index=self._heap.index(parent)
        _child_index=_parent_index * 2 + 1
        if not _child_index > len(self._heap):
            return self._heap[_child_index]
        else:
            raise Exception

    def get_right_child(self,parent):
        _parent_index=self._heap.index(parent)
        _child_index=_parent_index * 2 + 2
        if not _child_index > len(self._heap):
            return self._heap[_child_index]
        else:
            raise Exception

    def get_parent(self,child):
        _child_index=self._heap.index(child)
        _parent_index=(_child_index -1 )/2
        if not _parent_index < 0:
            return _parent_index, self._heap[_parent_index]
        else:
            raise Exception

    def get_child_index(self,parent_index):
        return (parent_index * 2 + 1), (parent_index * 2 + 2)

    def get_parent_index(self,child_index):
        return (child_index - 1 )/2


    def add(self,child):
        self._heap.append(child)
        _child_index = len(self._heap) - 1
        while _child_index > 0:
          _parent_index = self.get_parent_index(_child_index)
          if self._heap[_parent_index] > self._heap[_child_index]:
              self._heap[_parent_index], self._heap[_child_index] = self._heap[_child_index], self._heap[_parent_index]
          _child_index = _parent_index

    def delete(self):
        self._heap[0] = self._heap[len(self._heap) - 1]
        #del self._heap.pop[len(self._heap) - 1]
        parent_index = 0
        while parent_index < len(self._heap):
          l_child_index, r_child_index = self.get_child_index(parent_index)
          if l_child_index < len(self._heap):
              if self._heap[parent_index] > self._heap[l_child_index]:
                  self._heap[parent_index], self._heap[l_child_index] = self._heap[l_child_index], self._heap[parent_index]
                  parent_index = l_child_index
          elif r_child_index < len(self._heap):
              if self._heap[parent_index] > self._heap[r_child_index]:
                  self._heap[parent_index], self._heap[r_child_index] = self._heap[r_child_index], self._heap[parent_index]
                  parent_index = r_child_index
          else:
              parent_index, _ = self.get_child_index(parent_index)











