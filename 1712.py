
import sys

a,b,c = map(int, sys.stdin.readline().split())

answer = -1

if c-b > 0:
    answer = a//(c-b)+1

print(answer)