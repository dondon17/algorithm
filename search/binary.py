def binarysearch(item, stock, start, end):
    while start<=end:
        mid = (start+end) // 2
        if stock[mid] == item: 
            return "Yes"
        elif stock[mid] > item:
            end = mid-1
        else:
            start = mid+1
    return "NO"

n = int(input())
stock = list(map(int, input().split()))
stock.sort()

m = int(input())
need = list(map(int, input().split()))

for e in need:
    print("item: {} / stock: {}".format(e, binarysearch(e, stock, 0, n-1)))