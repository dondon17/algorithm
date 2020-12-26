# # 입력하고 싶은만큼 숫자를 입력해 바로 배열에 넣는 방법
# arr = [int(x) for x in input().split()] 

# for num in arr:
#     if num==0: break
#     else: print(num)

x = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%s" %(x, i, format(x*i, 'X')))