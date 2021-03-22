def solution(arr, n):
    tmp = ""
    for e in arr:
        tmp += e[0]*e[1]
    chunks, chunk_size = len(tmp), 10
    return [tmp[i:i+chunk_size] for i in range(0, chunks, chunk_size)]



t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        c, m = input().split()
        arr.append([c, int(m)])
        
    print("#{}".format(i))
    answer = solution(arr, n)
    for e in answer:
        print(e)
