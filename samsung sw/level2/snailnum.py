def printarr(arr):
    for r in arr:
        for e in r:
            print(e, end=" ")
        print()

def solution(size):
    snailarr = [[0 for _ in range(size)] for _ in range(size)]
    val = 0

    x, y = 0, -1
    sw = 1

    while True:
        for _ in range(size):
            val += 1
            y += sw
            snailarr[x][y] = val
            
        size -= 1
        if size == 0: break

        for _ in range(size):
            val += 1
            x += sw
            snailarr[x][y] = val
            
        sw *= -1
         
        for _ in range(size):
            val += 1
            y += sw
            snailarr[x][y] = val
            
        size -= 1
        if size == 0: break
        for _ in range(size):
            val += 1
            x += sw
            snailarr[x][y] = val
            
        sw *= -1

    printarr(snailarr)



        
t = int(input())
for i in range(1, t+1):
    size = int(input())
    print("#{}".format(i))
    solution(size)