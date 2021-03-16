t = int(input())

for i in range(1, t+1):
    answer = 0
    n, k = map(int, input().split())
    pan = []

    for j in range(n):
        pan.append(list(map(int, input().split())))

    # 가로 탐색
    for a in range(n):
        stackw = []
        stackh = []
        flag = 0

        for b in range(n):
            if pan[a][b] == 1:
                stackw.append((a,b))

            if pan[b][a] == 1:
                stackh.append((b,a))

            else: 
                flag = 1
                continue

        if len(stackh) == k: answer+=1
        if len(stackw) == k: answer+=1
    print("#{} {}".format(i, answer))