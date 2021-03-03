from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        new = queue.popleft()
        print(new, end=' ')
        for adj in graph[new]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

visited=[False]*9
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
] 
for g in graph:
    print(g)
bfs(graph, 1, visited)
