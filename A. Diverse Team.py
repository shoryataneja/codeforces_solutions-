n,k = map(int,input().split())
arr = list(map(int,input().split()))

lst = []

for i in range(n):
    is_first = True
    for j in range(i):
        if arr[i] == arr[j]:
            is_first = False
            break
    if is_first:
        lst.append(i+1)

if len(lst) == k:
    print("YES")
    print(*lst)
else:
    print("NO")