n = int(input())
ages = []
for i in range(n):
    age, name = map(str, input().split())
    ages.append({'age': int(age), 'name': name})

ages = sorted(ages.items(), key)
