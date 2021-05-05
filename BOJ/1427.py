n = int(input())

arr = []

while n>0:
    arr.append(n%10)
    n//=10

arr.sort(reverse=True)
print("".join(map(str, arr)))