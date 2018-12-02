
def DFS(g, s, visited):
  print s
  visited[s] = True
  for i in range(len(g)):
    v = g[s][i]
    if v == 1 and visited[i] == False:
      DFS(g, i, visited)
    


graph = [ 
  [0, 1, 0],
  [1, 0, 1],
  [0, 1, 0],
]

n = len(graph)
visited = [False for i in range(n)]

DFS(graph, 1, visited)

