n = int(input())
arr = list(map(int,input().split()))

arr.sort()

larg_ele = arr[-1]

ans = 0 

for i in range(n):
    ans += abs(arr[i]-larg_ele)

print(ans)

