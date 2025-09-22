# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     for i in range(n):
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 del arr[i]
#                 del arr[j]
#     print (len(arr))

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique = len(set(arr))
    duplicates = n - unique
    
    if duplicates % 2 == 0:
        print(unique)
    else:
        print(unique - 1)
