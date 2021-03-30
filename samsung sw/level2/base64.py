
def solution(p):
    pnum = []
    binpnum = []
    decpnum = []
    answer = ""
    for ch in p:
        if ch >= 'A' and ch <= 'Z': 
            pnum.append(ord(ch)-65)
        elif ch >= 'a' and ch <= 'z':
            pnum.append(ord(ch)-71)
        elif ch >= '0' and ch <= '9':
            pnum.append(ord(ch)+4)
        else: 
            if ch == "+": pnum.append(62)
            elif ch == "/": pnum.append(63)

    # print(pnum)
    cnt = 0
    longbin = ""
    for sb in pnum:
        longbin += format(sb, '06b')
        cnt += 1
        if cnt == 4:
            binpnum.append(longbin)
            cnt = 0
            longbin = ""
    # print(binpnum)

    start = 7
    for binary24 in binpnum:
        tmp = [chr(int(binary24[i:i + 8], 2)) for i in range(0, len(binary24), 8)]
        for c in tmp:
            answer += c

    return answer 

    
t = int(input())
for i in range(1, t+1):
    answer = ""
    p = input()
    answer = solution(p)
    print("#{} {}".format(i, answer))