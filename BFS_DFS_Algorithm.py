graph = {
   'A': ['B','C'],
   'B': ['A','C','D'],
   'C': ['A','B','D','E'],
   'D': ['B','C','E','F'],
   'E': ['C','D'],
   'F': ['D']
}

def BFS(graph, start):
   queue = []
   queue.append(start)
   seen = set()
   seen.add(start)

   while(len(queue) > 0):
      vertex = queue.pop(0)
      nodes = graph[vertex]
      for w in nodes:
         if w not in seen:
            queue.append(w)
            seen.add(w)
      print(vertex)

def DFS(graph, start):
   stack = []
   stack.append(start)
   seen = set()
   seen.add(start)

   while(len(stack) > 0):
      vertex = stack.pop()
      nodes = graph[vertex]
      for w in nodes:
         if w not in seen:
            stack.append(w)
            seen.add(w)
      print(vertex)

BFS(graph, 'A')
print('new line')
DFS(graph, 'A')