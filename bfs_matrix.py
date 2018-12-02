
def BFS(g, s, visited):
  stack = [s]
  while len(stack) > 0:
    v = stack.pop(0)
    visited[v] = True
    print v
    for i in range(len(g)):
      if visited[i] == True or i in stack:
        continue
      if g[v][i] == 1:
        stack.append(i)
  

graph = [
  [1, 1, 1, 0],
  [0, 1, 1, 0],
  [0, 1, 1, 1],
  [1, 1, 0, 1],
]

n = len(graph)
visited = [False for i in range(n)]

BFS(graph, 1, visited)

