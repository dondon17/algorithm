def checkrow(pan):
    for i in range(len(pan)):
        checkrow = [0]*9
        for j in range(len(pan)):
            checkrow[pan[i][j]-1] = 1
        for c in checkrow:
            if c != 1:
                return False
    return True
        
def checkcol(pan):
    for j in range(len(pan)):
        checkcol = [0]*9
        for i in range(len(pan)):
            checkcol[pan[i][j]-1] = 1
        for c in checkcol:
            if c != 1:
                return False
    return True

def checkbox(pan):
    for i in range(len(pan)):
        if i % 3 != 0: continue
        for j in range(len(pan)):
            if j % 3 != 0: continue 
            checkbox = [0]*9
            for k in range(i, i+3):
                for l in range(j, j+3):
                    checkbox[pan[k][l]-1] = 1
                #     print(pan[k][l], end="")
                # print()
            for c in checkbox:
                if c != 1: return False
    return True
        




t = int(input())
for i in range(1, t+1):
    answer = 0
    pan = []
    for _ in range(9): pan.append(list(map(int, input().split())))
    if checkrow(pan) and checkcol(pan) and checkbox(pan): answer = 1
    # if checkbox(pan): answer = 1
    print("#{} {}".format(i, answer))