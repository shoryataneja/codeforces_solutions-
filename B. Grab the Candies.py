t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    even_sum = 0 
    odd_sum = 0 
    for i in range(n):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
        else:
            odd_sum += lst[i]
    
    if even_sum > odd_sum:
        print("yes")
    elif even_sum == odd_sum:
        print("no")
    else:
        print("no")