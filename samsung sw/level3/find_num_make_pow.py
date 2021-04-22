dp = [0, 1. ]
def sol(n):
    arr = [0 for _ in range(n+1)]

    result = 1
    while n!=1:
        for j in range(2, n+1):
            if n%j == 0:
                arr[j] += 1
                n //= j
            else: 
                continue
            break


    for k in range(len(arr)):
        if arr[k] % 2 == 1:
            result *= k
        else: 
            continue
    
    return result


t = int(input())

for i in range(1, t+1):
    n = int(input())
    answer = sol(n)
    print("#{} {}".format(i, answer))