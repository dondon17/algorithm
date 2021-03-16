def solution(grades, n, k):
    if (n % 10 != 0) or (k < 1 or k > n): return -1
    cnt = 0
    j = 0

    grade_alpha = ["D0", "C-", "C0", "C+", "B-", "B0", "B+", "A-", "A0", "A+"]    

    sorted_grades = [v for (v, i) in sorted((v, i) for (i, v) in enumerate(grades))]
    sorted_grades_idx = [i+1 for (v, i) in sorted((v, i) for (i, v) in enumerate(grades))]
    
    for i in range(n):
        if cnt == n//10: 
            j += 1
            cnt = 0

        sorted_grades[i] = (sorted_grades[i], grade_alpha[j])
        cnt+=1


    return sorted_grades[sorted_grades_idx.index(k)][1]



t = int(input())
for i in range(1, t+1):
    answer = ""
    avggrades = []
    n, k = map(int, input().split())
    for j in range(1, n+1):
        eachgrades = list(map(int, input().split()))
        avggrades.append(eachgrades[0]*0.35 + eachgrades[1]*0.45 + eachgrades[2]*0.2)
    answer += solution(avggrades, n, k)
    print("#{} {}".format(i, answer))