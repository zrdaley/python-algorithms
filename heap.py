#!/usr/bin/python

class MinHeap:
  def __init__(self, values=[]):
    self.heap = [0]
    self.size = 0
    for value in values:
      self.insert(value)

  def bubble_up(self, n):
    while (n // 2) > 0:
      parent = self.heap[n // 2]
      child = self.heap[n]
      if parent > child:
        self.heap[n] = parent
        self.heap[n // 2] = child
      n = n // 2

  def insert(self, value):
    self.heap.append(value)
    self.size += 1
    self.bubble_up(self.size)

  def minChild(self,i):
    if i * 2 + 1 > self.size:
      return i * 2
    else:
      if self.heap[i*2] < self.heap[i*2+1]:
        return i * 2
      else:
          return i * 2 + 1

  def bubble_down(self, i):
    while (i * 2) <= self.size:
      child_index = self.minChild(i)
      child = self.heap[child_index]
      parent = self.heap[i]
      if parent > child:
        self.heap[i] = child
        self.heap[child_index] = parent
      i = i * 2

  def delete_min(self):
    if self.size == 0:
      return None
    
    top = self.heap[1]
    if self.size == 1:
      self.size -= 1
      self.heap = [0]
    else:
      self.heap[1] = self.heap[self.size]
      self.heap = self.heap[:-1]
      self.size -= 1
      self.bubble_down(1)
    return top

def main():
  values = raw_input("Please enter values to be turned into a heap:\n").split()
  
  heap = MinHeap(values)

  v = heap.delete_min()
  while v is not None:
    print v
    v = heap.delete_min()

if __name__ == "__main__":
   main()