n = int(input())
arr = list(map(int,input().split()))
x = int(input())

if x in arr:
    print(arr.index(x))
else:
    print(-1)