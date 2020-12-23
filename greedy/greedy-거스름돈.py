# 그리디 - 거스름돈
price = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
total = 0
for cash in money:
    total += (price//cash)
    price %= cash

print(total)
