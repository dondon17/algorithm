def sol(n, m):
    if m == 0:
        return 1;
    return n*sol(n, m-1)

for i in range(1, 11):
    t = int(input())
    n, m = map(int,input().split())
    answer = sol(n, m)
    print("#{} {}".format(i, answer))

