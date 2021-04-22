def sol(arr):
    
    end = len(arr)
    _max = arr[0]
    start, last = 0, 1
    while(True):
        if start >= end: 
            break
        if last > end:
            last = start + 1
            start += 1

        # tmp = sum(arr[start:last])

        # _max = _max if _max > tmp else tmp
        print(arr[start:last])
        last += 1

    return _max


t = int(input())
for i in range(1, t+1):
    s = int(input())
    arr = list(map(int, input().split()))
    answer = sol(arr)
    # print("#{} {}".format(i, answer))