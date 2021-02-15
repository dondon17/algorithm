word = input()

cnt0, cnt1 = 0, 0
flag1, flag0 = 1, 1

for i in range(len(word)):
    if word[i] == '1' and flag1 == 1:
        flag1 = 0
        flag0 = 1
        cnt1 += 1

    if word[i] == '0' and flag0 == 1:
        flag0 = 0
        flag1 = 1
        cnt0 += 1

print(min(cnt0, cnt1))