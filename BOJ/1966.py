'''
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
'''


from collections import deque

tc = int(input())

for i in range(1, tc+1):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    queue = [(val, idx) for idx, val in enumerate(queue)]


    answer = 0
    
    while queue:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            answer += 1
            if queue[0][1] == m:
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
    print(answer)