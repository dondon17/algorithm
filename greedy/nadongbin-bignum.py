# def solution(n, m, k):
#     answer = 0
#     cnt, tmp = 0, 0
#     nums = list(map(int, input().split(" ")))
#     nums.sort(reverse=True)

#     _max = nums[0]
#     _next = nums[1]

#     while True:
#         if cnt >= m:
#             break


#         if tmp < k:
#             answer += _max
#             tmp += 1
#         elif tmp == k:
#             tmp = 0
#             answer += _next

#         cnt += 1 
#         print(cnt, answer)
#     return answer

# n, m, k = map(int, input().split(" "))
# print(solution(n,m,k))



#다른 풀이
def solution(n,m,k):
    answer = 0
    nums = list(map(int, input().split(" ")))
    nums.sort()

    _max = nums[n-1]
    _next = nums[n-2]

    # 가장 큰 수가 더해지는 횟수
    cnt = m - m//(k+1)

    # 두번째 수가 더해지는 횟수
    cnt2 = m//(k+1)
    answer = cnt*_max + cnt2*_next 
    return answer    

n, m, k = map(int, input().split(" "))
print(solution(n,m,k))
