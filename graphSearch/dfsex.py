from collections import deque

n, m, v = map(int, input().split())

graph = [[]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, nv = map(int, input().split())
    graph[a].append(nv)

def dfs(graph, k, visited):
    visited[k] = True
    print(k, end=" ")
    for i in graph[k]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, m, visited):
    queue = deque([m])
    visited[m] = True

    while queue:
        new = queue.popleft() 
        print(new, end=' ')
        for b in graph[new]:
            if not visited[b]:
                queue.append(b)       
                visited[b] = True
    print()

dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited)