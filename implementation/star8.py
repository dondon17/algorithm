n = int(input())

for i in range(1, 2*n):
    if i <= n:
        for j in range(i):
            print("*", end="")

        for k in range(2*(n-i)):
            print(" ", end="")
        
        for m in range(i):
            print("*", end="")
        
        print("")
    
    else:
        for j in range(2*n-i):
            print("*", end="")

        for k in range(2*(i-n)):
            print(" ", end="")
        
        for m in range(2*n-i):
            print("*", end="")
        
        print("")
