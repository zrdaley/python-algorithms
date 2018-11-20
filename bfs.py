#!/usr/bin/python

def graph_bfs(graph, start):
  stack = [start]
  visited = []

  while stack:
    s = stack.pop(0)
    visited.append(s)
    for v in graph[s]:
      if v in visited or v in stack:
        continue      
      stack.append(v)
  return visited
      

def matrix_bfs(matrix, start):
  stack = [start]
  visited = []

  while stack:
    y = stack.pop(0)
    visited.append(y)
    for x, v in enumerate(matrix[y]):
      if v == 1:
        if x in visited or x in stack:
          continue
        stack.append(x)
  return visited

  
def main():
  graph = {}
  graph[0] = [1,2]
  graph[1] = [2]
  graph[2] = [1, 3]
  graph[3] = [0, 1] 

  print graph_bfs(graph, 1)

  matrix = [
  [1, 1, 1, 0],
  [0, 1, 1, 0],
  [0, 1, 1, 1],
  [1, 1, 0, 1],
  ]

  print matrix_bfs(matrix, 1)


if __name__ == "__main__":
   main()

