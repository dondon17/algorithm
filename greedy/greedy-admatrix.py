import numpy

n, m = map(int, input().split(" "))
src = numpy.array()
des = numpy.array()

flag = 0

# tmp = ""
# test = ["1111", "0011"]
# for i in test[1]:
#     tmp += str(int(i) ^ 1)
# print(tmp) 

for i in range(2*n):
    if i<n:
        src.append((input()))
    else:
        des.append((input()))

print(src[0:2, 0:2])