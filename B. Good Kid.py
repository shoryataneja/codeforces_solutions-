# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     k = arr[-1] + 1 
#     for i in range(n):
#         if arr[i] == 0:
#             arr[i] += 1 
#             break
#         else:
#             arr[-1] = k 
#     p = 1 
#     for i in arr:
#         p *= i 
#     print(p)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxp = 0 
    for k in range(n):
        arr[k] += 1 
        p = 1
        for val in arr:
            p *= val
        maxp = max(p,maxp)
        arr[k] -= 1 
    print(maxp)
