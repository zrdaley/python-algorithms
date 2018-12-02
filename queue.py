#!/usr/bin/python

from stack import Node

class Queue:
  def __init__(self, values):
    if len(values) == 0:
      self.top = None
      return
  
    self.top = Node(values[-1])
    if len(values) == 1:
      self.bottom = self.top

    prev = self.top
    for val in values[1::-1]:
      node = Node(val)
      node.prev = prev
      prev.next = node
      prev = node
    self.bottom = node
    
  
  def pop(self):
    temp = self.bottom

    #empty case
    if temp is None:
      return None
    
    # only 1 element case
    if temp.prev is None:
      self.bottom = None
      self.top = None
    else:
      self.bottom = temp.prev
      self.bottom.next = None
    return temp
  
  
  def push(self, val):
    new = Node(val)
    new.next = self.top
    self.top.prev = new
    self.top = new


def main():
  values = raw_input("Please enter values to be turned into a queue:\n").split()
  q = Queue(values)

  q.push("x")

  v = q.pop()
  while v is not None:
    print v.value
    v = q.pop()

if __name__ == "__main__":
   main()