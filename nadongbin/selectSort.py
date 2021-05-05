'''
선택 정렬
: 무작위 수로 구성된 배열에서 첫번째 인덱스부터 시작해 가장 작은 값을 가장 앞의 인덱스와 바꿔가며 정렬하는 방식
예시)
7 5 9 0 3 1 6 2 4 8
1) 0 5 9 7 3 1 6 2 4 8 - 7과 0 swap
2) 0 1 9 7 3 5 6 2 4 8 - 5와 1 swap
3) 0 1 2 7 3 5 6 9 4 8 - 9와 2 swap
...

O(n) = n^2
'''
from random import *

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    minIdx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minIdx]:
            minIdx = j
    # temp = arr[i]
    # arr[i] = arr[minIdx]
    # arr[minIdx] = temp
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
    print("#{}. {}".format(i+1, arr))
