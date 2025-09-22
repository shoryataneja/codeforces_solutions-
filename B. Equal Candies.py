t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = sorted(arr)
    n = len(k)
    f_e = k[0]
    
    min_candy = 0

    for i in range(n):
        o = abs(f_e - k[i] )
        min_candy += o 
    print(min_candy)u