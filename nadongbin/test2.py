'''
U X: 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
D X: 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
C : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
Z : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

n : 표의 행 개수
k : 처음 선택된 행의 위치
cmd : 명령어

결국 달라지는 문자는 C와 Z 명령어의 차이만큼 발생
'''

from collections import deque, Counter

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","U 2","Z","Z","U 1", "C"]

def solution(n, k, cmd):
    answer = ''
    temp = [1 for _ in range(n)]
    pointer = k                 # 현재 위치 가리킬 변수
    removeinfo = deque([])      # 삭제된 인덱스 정보 가리킬 변수
    
    if Counter(cmd)['C'] == Counter(cmd)['Z']:
        return temp

    for command in cmd:
        # 명령어와 이동시킬 인덱스 초기화
        c = command[0]
        idx = "" if len(command) < 2 else int(command[-1])
        cnt = 0

        # 범위 내에서만 이동시키므로, 인덱스를 벗어나는 경우는 없다고 가정
        if c == 'D':
            if -1 in temp[pointer:pointer+idx+1]:
                # Xcount = Counter(temp[pointer:pointer+idx+1])['X']
                Xcount = temp[pointer:pointer+idx+1].count(-1)
                pointer += Xcount
            pointer += idx

        elif c == 'U':
            #우선 인덱스만큼 빼고, 범위 내에 x의 개수만큼 추가로 더 빼줌
            if -1 in temp[pointer-idx:pointer]:
                # Xcount = Counter(temp[pointer-idx:pointer])['X']
                Xcount = temp[pointer-idx:pointer].count(-1)
                pointer -= Xcount
            pointer -= idx

        elif c == "C":
            # 현재 가리키는 위치를 x표시하고 스택에 삭제한 인덱스 추가
            temp[pointer] = -1
            removeinfo.append(pointer) 
            # 삭제한 인덱스의 아래칸이 범위 내면 한칸 아래로, 만약 포인터가 마지막인덱스라면 -1
            if pointer == n-1:
                pointer -= 1
            else: 
                pointer += 1
        
        elif c == "Z":
            temp[removeinfo.pop()] = 1
    answer = ''
    for n in temp:
        if n == 1:
            answer += 'O'
        else:
            answer += 'X'
    return answer


print(solution(n,k,cmd))