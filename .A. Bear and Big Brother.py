a,b = map(int,input().split())

ans = 0 

for i in range(10):
    a = 3*a
    b = 2*b 
    ans += 1 
    if a > b:
        break
print(ans)