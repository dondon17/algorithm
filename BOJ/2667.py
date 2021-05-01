mapSize = int(input())
graph = []
part = 0
count = 0
counts = []
for _ in range(mapSize):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global count
    if x<0 or y<0 or x>=mapSize or y>=mapSize:
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    
    return False

for i in range(mapSize):
    for j in range(mapSize):
        if dfs(i, j) == True:
            part += 1
            counts.append(count)
        else:
            count = 0

print(part)

for cnt in sorted(counts):
    print(cnt)