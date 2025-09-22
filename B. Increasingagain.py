t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = True
    if len(set(arr)) == n:
        print("yes")
    else:
        print("no")