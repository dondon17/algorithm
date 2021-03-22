def turn90(arr, n):
    _90 = []
    _180 = []
    _270 = []
    cv = 0
    for i in range(n):
        for j in range(n):
            _90.append(arr[n-1-j][i])
    
    for i in range(n):
        for j in range(n):
            _180.append(arr[n-1-i][n-1-j])

    for i in range(n):
        for j in range(n):
            _270.append(arr[j][n-1-i])

    for i in range(n):
        for j in range(n):
            print(_90[cv+j], end="")
        print(" ", end="")

        for j in range(n):
            print(_180[cv+j], end="")
        print(" ", end="")

        for j in range(n):
            print(_270[cv+j], end="")
        print()
        cv += n

t = int(input())

for i in range(1, t+1):
    n = int(input())
    pan = []
    for _ in range(n):
        pan.append(list(map(int, input().split())))
    print("#{}".format(i))
    turn90(pan, n)