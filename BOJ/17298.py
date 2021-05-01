n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(n)]

stack.append(0)
idx = 1

while stack and idx<n:
    while stack and arr[stack[-1]] < arr[idx]:
        answer[stack[-1]] = arr[idx]
        stack.pop()
    stack.append(idx)
    idx+=1

print(*answer)
