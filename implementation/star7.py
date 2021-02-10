n = int(input())

for i in range(1, 2*n):
    if i <= n:
        for j in range(n-i):
            print(" ", end="")

        for k in range(2*i-1):
            print("*", end="")
        
        print("")
    
    else:
        for k in range(i-n):
            print(" ", end="")
        
        for m in range(2*n-2*(i-n)-1):
            print("*", end="")
        
        print("")
