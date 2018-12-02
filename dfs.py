#!/usr/bin/python

def graph_dfs(graph, start):
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
  
def main():
  graph = {}
  graph[0] = [1,2]
  graph[1] = [2]
  graph[2] = [1, 3]
  graph[3] = [0, 1] 

  print graph_dfs(graph, 1)


if __name__ == "__main__":
   main()

