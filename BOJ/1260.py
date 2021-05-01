from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
sortedgraph = [[]]

for idx in range(1, m+1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
for l in graph:
    l.sort()


visited = [False]*(n+1)
dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited)
print()


