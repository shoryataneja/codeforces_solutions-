n,h = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0 

for i in range(n):
    if arr[i] <= h:
        ans += 1 
    else : 
        ans += 2

print(ans)
