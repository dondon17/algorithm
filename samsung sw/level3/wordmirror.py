def solution(word):
    result = ""
    for i in range(len(word)-1, -1, -1):
        c = word[i]
        if c == 'p': result += 'q'
        elif c == 'q': result += 'p'
        elif c == 'b': result += 'd'
        elif c == 'd': result += 'b'
    return result

t = int(input())

for tc in range(1, t+1):
    word = input()
    answer = solution(word)
    print("#{} {}".format(tc, answer))