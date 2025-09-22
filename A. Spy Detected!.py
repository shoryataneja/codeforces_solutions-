t = int(input())

for _ in range(t):
    a = int(input())
    arr = list(map(int,input().split()))

    if arr[0] == arr[1]:
        c_e = arr[0]
    elif arr[0] == arr[2]:
        c_e = arr[0]
    else:
        c_e = arr[1]
    
    for i in range(a):
        if arr[i] != c_e:
            print(i+1)
            break