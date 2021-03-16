def solution(p):
    plen = len(p)
    if p[:plen//2] == p[-1:-(plen//2+1):-1]: return True
    return False

t = int(input())

for i in range(1, t+1):
    answer = 0
    word = input()
    if solution(word): answer = 1
    print("#{} {}".format(i, answer))