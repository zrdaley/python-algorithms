#!/usr/bin/python

class Node:
  def __init__(self, val, parent):
    self.parent = parent
    self.left = None
    self.right = None
    self.value = val

class Tree:
  def __init__(self, values):
    self.top = Node(values[0], None)
    for value in values[1:]:
      self.insert(self.top, value)
  
  def insert(self, parent, value):
    if parent.value > value:
      if parent.left is not None:
        self.insert(parent.left, value)
      else:
        parent.left = Node(value, parent)
    elif parent.value < value:
      if parent.right is not None:
        self.insert(parent.right, value)
      else:
        parent.right = Node(value, parent)


  def find(self, val, start):
    curr = self.top
    while curr is not None:
      if curr.value == val:
        return curr
      if val > curr.value:
        curr = curr.right
      elif val < curr.value:
        curr = curr.left
    return None

  def delete(self, val):
    node = self.find(val, self.top)
    if node is None:
      print "delete(): Node does not exist in tree"
      return

    def _update_parent(node, updated):
      if node.parent is None:
        self.top = updated
      elif node == node.parent.right:
        node.parent.right = updated
      elif node == node.parent.left:
        node.parent.left = updated

    if node.right is None and node.left is None:
      _update_parent(node, None)
      return
    
    if node.right is None:
      _update_parent(node, node.left)
      return
    
    elif node.left is None:
      _update_parent(node, node.right)
      return

    # find successor
    s = node
    while s.right is not None:
      s = s.right
    
    node.value = s.value
    _update_parent(s, None)


  def print_in_order(self, node):
    if node is None:
      return
    self.print_in_order(node.left)
    print node.value
    self.print_in_order(node.right)


def main():
  values = raw_input("Please enter values to be turned into a bst: ").split()
  bst = Tree(values)
  bst.print_in_order(bst.top)

  to_delete = raw_input("Please enter a value to delete: ")
  bst.delete(to_delete)
  bst.print_in_order(bst.top)


if __name__ == "__main__":
   main()