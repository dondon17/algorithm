'''
1 이상 N 이하의 정수가 적혀 있는 길이 N의 순열 p1, p2, …, pN이 있다. 수열에 있는 모든 숫자는 서로 다르다. 
2 ≤ i ≤ N-1이며, pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi를 평범한 숫자라고 정의한다. 
주어진 순열에서 평범한 숫자의 개수는 몇 개인가?

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
    ∙ 첫 번째 줄에 정수 N 이 주어진다. (3 ≤ N ≤ 20)
    ∙ 이후 N개의 정수 pi가 주어진다. (3 ≤ pi ≤ N) 모든 pi는 서로 다르다.

[출력]
각 테스트 케이스마다 정답을 출력하라.
'''
def solution(n, pi):
    answer = 0
    for i in range(n-2):
        temp = pi[i:i+3]
        if temp[1] != max(temp) and temp[1] != min(temp):
            answer += 1
        else: 
            continue

    return answer

tc = int(input())

for i in range(1, tc+1):
    n = int(input())
    pi = list(map(int, input().split()))
    answer = solution(n, pi)
    print("#{} {}".format(i, answer))