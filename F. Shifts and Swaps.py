t = int(input())

for _ in range(t):
    n,m = map(int,input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    while a == b:
        f_e = a[0]
        for i in range(1,n):
            a[i] = a[i-1]
        a[n-1] = f_e
