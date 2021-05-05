'''
# itertools 라이브러리의 permutation 함수 사용 방법
import itertools

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
answer = list(itertools.permutations(nums, m))

for e in answer:
    print(' '.join(map(str, e)))
'''

