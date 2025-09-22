n = int(input())
arr = list(map(int,input().split()))
# arr.sort()
all_same = True 

for i in range(1,len(arr)):
    if arr[i] != arr[0]:
        all_same = False
        break 
    else:
        continue

if all_same == True:
    print(1)
    print(arr[0])
else:
    for i in range(n-1,-1,-1):
        for j in range(i - 1, -1,-1):
            if arr[j] == arr[i]:
                arr[j] = None  
    new_arr = []
    for x in arr:
        if x != None:
            new_arr.append(x)
    print(len(new_arr))
    print(*new_arr) 