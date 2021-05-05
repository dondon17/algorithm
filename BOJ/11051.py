def coefficient(n, k):
    return (factorial(n)//factorial(k)//factorial(n-k))%10007


def factorial(n):
    if n <= 1: 
        return 1
    else:
        return n*factorial(n-1)

n, k = map(int, input().split())

print(coefficient(n, k))

