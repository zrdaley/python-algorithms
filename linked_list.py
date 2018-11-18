#!/usr/bin/python

class Node:
  def __init__(self, x):
    self.next = None
    self.value = x
  
  def append(self, n):
    self.next = n
  
  def update_value(self, x):
    self.value = x

class LinkedList:
  def __init__(self, values):
    self.head = Node(values[0])
    curr = self.head
    for value in values[1:]:
      curr.append(Node(value))
      curr = curr.next
  
  def print_list(self):
    l = ""
    curr = self.head
    while curr:
      l += curr.value
      if curr.next != None:
        l += " -> "
      curr = curr.next
    print l
  
def main():
  values = raw_input("Please enter values to be turned into a linked list:\n").split()
  linked_list = LinkedList(values)
  linked_list.print_list()

if __name__ == "__main__":
   main()
