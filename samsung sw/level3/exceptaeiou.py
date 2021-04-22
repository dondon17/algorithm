def sol(word):
    arr = ['a', 'e', 'i', 'o', 'u']
    flag =0
    result = ""
    for c in word:
        if c not in arr:
            result += c
    return result
        

t = int(input())
for i in range(1, t+1):
    word = input()
    answer = sol(word)
    print("#{} {}".format(i, answer))