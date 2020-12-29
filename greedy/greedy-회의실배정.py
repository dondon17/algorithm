n = int(input())
meeting = []
for i in range(n):
    start_time, end_time = map(int, input().split())
    meeting.append((start_time, end_time))

meetcnt1 = 0
start_time= 0

meeting = sorted(meeting, key=lambda time: time[0])
for time in meeting:
    if time[0] >= start_time:
        start_time = time[1]
        meetcnt1+=1


meetcnt2 = 0
start_time= 0
meeting = sorted(meeting, key=lambda time: time[1])
for time in meeting:
    if time[0] >= start_time:
        start_time = time[1]
        meetcnt2+=1

print(meetcnt1 if meetcnt1>=meetcnt2 else meetcnt2)