for i in range(1, 11):
    arr = []
    l = int(input())
    answer = 0
    for _ in range(8):
        arr.append(list(input()))

    for r in range(8):
        for c in range(8-l+1):
            row = arr[r][c:c+l]
            if l%2 == 0:
                r1 = row[:l//2]
                r2 = row[l-1:(l//2)-1:-1]

            else:
                r1 = row[:l//2]
                r2 = row[l-1:(l//2):-1]

            if r1==r2:
                # print(row)
                answer += 1
    
    for c in range(8):
        for r in range(9-l):
            col = ""
            for k in range(r, r+l):
                col += arr[k][c]

                if l%2 == 0:
                    c1 = col[:l//2]
                    c2 = col[l-1:(l//2)-1:-1]

                else:
                    c1 = col[:l//2]
                    c2 = col[l-1:(l//2):-1]

                if c1==c2:
                    answer += 1

    print("#{} {}".format(i, answer))