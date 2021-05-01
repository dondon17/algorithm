answer = []

def dfs(graph, start, visited):
    global answer
    visited[start] = True
    # print(start, end = " ")
    for i in graph[start]:
        if not visited[i]:
            answer.append(i)
            dfs(graph, i, visited)


computers = int(input())
edges = int(input())
networks = [[] for _ in range(computers+1)]

visited = [False for _ in range(computers+1)]

for _ in range(edges):
    v1, v2 = map(int, input().split())
    networks[v1].append(v2)
    networks[v2].append(v1)

dfs(networks, 1, visited)
print(len(answer))