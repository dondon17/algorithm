# 숫자로 이루어진 문자열에서 처음부터 + 또는 x 를 실행하여 가장 큰 수를 만들기
arr = str(input())
sum = int(arr[0])

for i in range(1, len(arr)):
    num = int(arr[i])
    if int(arr[i-1]) <= 1: sum += num
    else: sum *= num

print(sum)