t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    count = 0 
    max_count = 0 
    for i in arr:
        if i == 0:
            count += 1 
            max_count = max(count,max_count)
        else:
            count = 0 
    print(max_count)