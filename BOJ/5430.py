'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
'''

from collections import deque, Counter
    
t = int(input())
for _ in range(t):
    cmd = [c for c in input()]
    n = int(input())
    nums = input()
    arr = deque([])
    flag = 1
    # print(nums.strip()[1:-1])
    if n == 0:
        nums = []
    else:    
        arr = deque(list(map(int, nums.strip()[1:-1].split(','))))

    di = 1
    for p in cmd:
        if p == 'R':
            di *= -1
        elif p == 'D': 
            if arr:
                if di == 1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                flag = -1
                break
    if flag == 1:
        if di == 1:
            print("["+",".join(list(map(str, arr)))+"]")
        else:
            arr.reverse()
            print("["+",".join(list(map(str, arr)))+"]")

    else:
        print("error")
    

    
        
