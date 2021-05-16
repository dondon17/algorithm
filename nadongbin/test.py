# 맨해튼 거리가 3이상으로 (2이하는 x)
# 단 파티션으로 구분되는 경우 맨해턴 거리가 2여도 허용(파티션이 아닌 테이블이 있는 경우는 x)

# 응시자: p
# 테이블: O
# 파티션: X

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

def solution(places):
    answer = []

    for room in places:                     # 각 room이 하나의 대기실
        persons = []                        # 각 room마다 사람이 있는 좌표 저장
        flag = 1                            # 위반하는 경우가 있을경우 0으로 변경

        for r in range(5):                  # 사람의 위치만 저장
            for c in range(5):
                if room[r][c] == 'P':
                    persons.append((r,c))

        if len(persons) >= 2:               # 최소 두명이 있을 때에만 자리지킴 판별 진행 (사람이 1명 이하면, 거리지킴 준수)
            for p1 in range(len(persons)-1):
                for p2 in range(p1+1, len(persons)):
                    # 각 사람의 x, y좌표는 persons[p1][0],persons[p1][1]로 접근
                    distance = abs(persons[p1][0]-persons[p2][0]) + abs(persons[p1][1]-persons[p2][1])
                    if distance < 2:
                        flag = 0
                        break
                    elif distance == 2:
                        #case 1. 같은 행 
                        # print("p1: ({}, {}) / p2: ({}, {})".format(persons[p1][0],persons[p1][1], persons[p2][0], persons[p2][1]))
                        if persons[p1][0] == persons[p2][0]: # 같은 행
                            if room[persons[p1][0]][abs(persons[p1][1]+persons[p2][1])//2] != 'X':
                                flag = 0
                                # print("같은 행인데 가운데가 x가 아니어서 에러 종료")

                        #case 2. 같은 열
                        elif persons[p1][1] == persons[p2][1]: # 같은 열
                            if room[abs(persons[p1][0]+persons[p2][0])//2][persons[p1][1]] != 'X':
                                flag = 0
                                # print("같은 열인데 가운데가 x가 아니어서 에러 종료")

                        # case 3. ㄱ자 
                        else:
                            if room[persons[p1][0]][persons[p2][1]] != 'X' or room[persons[p2][0]][persons[p1][1]] != 'X':
                                flag = 0
                                # print("ㄱ자인데 가운데가 x가 아니어서 에러 종료")
                    else:
                        continue
                    
                    
                    if flag == 0:
                        break
                if flag == 0:
                    break
        answer.append(flag) # 각 룸마다 위반사항이 있으면 flag가 0이 되있을 것이고, 그게 아니라면 1로 유지


    return answer


print(solution(places))