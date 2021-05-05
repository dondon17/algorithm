n = int(input())

start = 1
i = 1
while True:
    if n <= start: break
    start += 6*i
    i+=1

print(i)