n = int(input())

count = 1
result = 0

while True:
    if n <= count: break

    n -= count

    count += 1

# count 번째 수열에서 n번째가 바로 우리가 구하고자 하는 분수
if count % 2 == 1:
    result = str(count+1-n)+"/"+str(n)
elif count % 2 == 0:
    result = str(n)+"/"+str(count+1-n)

print(result)
    