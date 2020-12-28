# 그리디 - 펜션
n, m = map(int, input().split(" "))
room = []

for i in range(n):
    room.append(input())

s, t = map(int, input().split(" "))
zeros_list = [0]*m

def check_room(day_room_check):
    chroom = [0]*m
    
    for idx, ox in enumerate(day_room_check):
        if ox == 'O': chroom[idx]=1
    
    if chroom == zeros_list: return -1
    return chroom

def check_max_day(room):
    move = -1
    check_list=[0]*m
    for day_room_check in room:
        if check_list != zeros_list:
            for idx, r in enumerate(check_list):
                if r==1 and day_room_check[idx]=='X': check_list[idx]=0
        if check_list == zeros_list:
            move += 1
            check_list = check_room(day_room_check)

            if check_list == -1: return -1
    
    return move

room = room[s-1:t-1]
print(check_max_day(room))




