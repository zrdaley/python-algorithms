#!/usr/bin/python

class Node:
  def __init__(self, val):
    self.value = val
    self.next = None
    self.prev = None

class Stack:
  def __init__(self, values):
    if len(values) == 0:
      self.top = None
      return
  
    self.top = Node(values[-1])
    prev = self.top
    for val in values[1::-1]:
      node = Node(val)
      prev.next = node
      prev = node
    
  
  def pop(self):
    temp = self.top
    if self.top is None:
      return None
    self.top = self.top.next
    return temp
  
  def push(self, val):
    new = Node(val)
    new.next = self.top
    self.top = new


def main():
  values = raw_input("Please enter values to be turned into a stack:\n").split()
  stack = Stack(values)

  stack.push("q")

  v = stack.pop()
  while v is not None:
    print v.value
    v = stack.pop()

if __name__ == "__main__":
   main()