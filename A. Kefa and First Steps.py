n = int(input())
arr = list(map(int,input().split()))

cnt = 0
maxcnt = 0

for i in range(n):
    if arr[i] >= arr[i-1]:
        cnt += 1 
    else:
        cnt = 1
    maxcnt = max(cnt,maxcnt)
print(maxcnt)