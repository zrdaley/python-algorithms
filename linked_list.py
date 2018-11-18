#!/usr/bin/python

class Node:
  def __init__(self, x):
    self.next = None
    self.value = x
  
  def append(self, n):
    self.next = n
  
  def updateValue(self, x):
    self.value = x


def printLinkedList(head):
  l = ""
  curr = head
  while curr:
    l += curr.value
    if curr.next != None:
      l += " -> "
    curr = curr.next
  print l

  
values = raw_input("Please enter values to be turned into a linked list:\n").split()

head = Node(values[0])
curr = head
for value in values[1:]:
  curr.append(Node(value))
  curr = curr.next

printLinkedList(head)
