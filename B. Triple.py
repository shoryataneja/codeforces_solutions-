# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     freq = {}
#     for i in arr:
#         freq[i] = freq.get(i,0) + 1 
#         if freq[i] == 3:
#             print(i)
#             break 
#     else:
#         print(-1)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    dictt = {}
    ans = -1 

    for i in arr:
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1 
    
        if dictt[i] == 3:
            ans = i 
            break

    print(ans)

    