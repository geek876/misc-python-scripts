class Heap:

    def __init__(self, array, N):
        self._heap =  array
        self._max  = N
        self._descending_sorted = []

    def get_heap(self):
        return self._heap

    def get_child_index(self,parent_index):
        return (parent_index * 2 + 1), (parent_index * 2 + 2)

    def get_parent_index(self,child_index):
        return (child_index - 1 )/2


    def add(self,child):
        if self._max == len(self._heap):
            self.delete()
        self._heap.append(child)
        child_index = len(self._heap) - 1
        while child_index > 0:
          parent_index = self.get_parent_index(child_index)
          if self._heap[parent_index] > self._heap[child_index]:
              self._heap[parent_index], self._heap[child_index] = self._heap[child_index], self._heap[parent_index]
          child_index = parent_index

    def delete(self):
        minimum_value = self._heap[0]
        self._heap[0] = self._heap[-1]
        del self._heap[-1]
        if len(self._heap) > 1:
          self.balance()
        return minimum_value

    def balance(self):
        parent_index = 0
        while True:
          l_child_index, r_child_index = self.get_child_index(parent_index)

          # Both left and right child present
          if (l_child_index < len(self._heap)) and (r_child_index < len(self._heap)):
              if self._heap[l_child_index] < self._heap[r_child_index]:
                  smaller = l_child_index
              else:
                  smaller = r_child_index
          # Only left child present
          elif l_child_index < len(self._heap):
              smaller = l_child_index

          if  self._heap[smaller] < self._heap[parent_index]:
              self.get_heap()
              self._heap[parent_index], self._heap[smaller] = self._heap[smaller], self._heap[parent_index]
              parent_index = smaller
          else:
              break

    def sort(self):
        for i in range(0,len(self._heap)):
            self._descending_sorted.append(self.delete())
        return self._descending_sorted


if __name__ == '__main__':
    f = 'test.txt'
    N = 12
    h = Heap([],N)
    for line in open(f, 'r').readlines():
        h.add(float(line))
    print h.get_heap()
    for number in reversed(h.sort()):
        print number
