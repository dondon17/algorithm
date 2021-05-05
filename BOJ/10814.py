n = int(input())
students = []

for _ in range(n):
    age, name = input().split()
    students.append((int(age), name))

students = sorted(students, key=lambda x : (x[0], x.index(x[1])))

for p in students:
    print(" ".join(map(str, p)))