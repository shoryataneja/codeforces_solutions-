n = int(input())
ans = 0 

for _ in range(n):
    pi , qi = map(int,input().split())
    if qi-pi >= 2:
        ans +=1  
print(ans)

