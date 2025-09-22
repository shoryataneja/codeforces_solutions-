t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = 0 
    for i in arr:
        s += i 
    if s[-1] == 3 :
        print("yes")
    else:
        print("no")