n = int(input())

cnt = 0 
ans = -1

for i in range(6):
    if n % 5 == 0 :
        ans = int(n/5)
        break
    else:
        ans = (n//5)+1


print(ans)