n = int(input())
arr = list(map(int,input().split()))

ans = 0 
for i in range(n):
    if arr[i] == 1:
        ans += 1 
    else:
        continue 

if ans >= 1 :
    print("HARD")
else:
    print("EASY")
