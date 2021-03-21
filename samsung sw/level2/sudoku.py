def checkrow(pan):
    for row in pan:
        check = [0]*9
        for num in row:
            check[num-1] += 1
            if check[num-1] != 1:
                return False
    return True
        
def checkcol(pan):
    for c in range(9):
        check = [0]*9
        for r in range(9):
            check[pan[c][r]-1] += 1
            if check[pan[c][r]-1] != 1:
                return False
    return True

def checkbox(pan):
    for i in range(len(pan)):
        if i % 3 != 0: continue
        for j in range(len(pan)):
            if j % 3 != 0: continue 
            check = [0]*9
            for k in range(i, i+3):
                for l in range(j, j+3):
                    check[pan[k][l]-1] += 1
                    if check[pan[k][l]-1] != 1:
                        return False
    
    return True
        




t = int(input())
for i in range(1, t+1):
    answer = 0
    pan = []
    for _ in range(9): pan.append(list(map(int, input().split())))
    if checkrow(pan) and checkcol(pan) and checkbox(pan): answer = 1
    print("#{} {}".format(i, answer))