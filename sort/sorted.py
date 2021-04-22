n = int(input())
student = []

for i in range(n):
    data = input().split()
    student.append((data[0], int(data[1])))

print(student)

student = sorted(student, key=lambda student:student[1], reverse=True)

for p in student:
    print(p)