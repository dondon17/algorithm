n = int(input())                            # 총 노드 개수
nodes = list(map(int, input().split()))     # 노드 간 연결 관계
removeNode = int(input())                   # 삭제할 노드
adjList = [[0]*n for _ in range(n)]            # 각 노드의 연결리스트
visited = [0 for _ in range(n)]             # 각 노드의 방문 여부
cnt = 0                                     # leaf node 개수

# 인접리스트 생성
for i in range(n):
    if nodes[i] == -1:
        root = i
    else:
        adjList[i][nodes[i]] = 1
        adjList[nodes[i]][i] = 1

# 삭제할 노드와 관련된 부분을 인접리스트에서 삭제
for i in range(n):
    adjList[i][removeNode] = 0 
    adjList[removeNode][i] = 0 


def dfs(root):                                
    global cnt
    flag = 0
    visited[root] = 1
    for i in range(len(adjList[root])):
        if adjList[root][i] == 1 and visited[i] == 0:
            flag = 1
            dfs(i)
    
    if flag == 0:
        cnt += 1

if removeNode == root:
    print(0)
else:
    dfs(root)
    print(cnt)