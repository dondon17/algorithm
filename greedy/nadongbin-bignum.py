def solution(n, m, k):
    answer = 0
    cnt, tmp = 0, 0

    nums = list(map(int, input().split(" ")))
    nums.sort(reverse=True)

    _max = nums[0]
    _next = nums[1]

    while True:
        if cnt >= m:
            break

        if tmp < k:
            answer += _max
            tmp += 1
        elif tmp == k:
            tmp = 0
            answer += _next

        cnt += 1 
        print(cnt, answer)
    return answer

n, m, k = map(int, input().split(" "))
print(solution(n,m,k))

