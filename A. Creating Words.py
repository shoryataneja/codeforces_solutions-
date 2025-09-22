t = int(input())

for _ in range(t):
    a,b = map(str,input().split())
    a = list(a)
    b = list(b)
    a[0],b[0]=b[0],a[0]
    # a = str(a)

    print(*a,sep="",end=" ")
    print(*b,sep="")
   