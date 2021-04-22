from collections import Counter

def solution(word):
    result = ""
    temp = []
    flag = 0
    # countword = Counter(word)
    for c in Counter(word):
        if Counter(word)[c] % 2 == 1:
            flag = 1
            temp.append(c)
        else: 
            continue
    temp.sort()
    result = result.join(temp)

    if flag == 0:
        result = "Good"

    return result

t = int(input())
for tc in range(1, t+1):
    word = input()
    answer = solution(word)
    print("#{} {}".format(tc, answer))