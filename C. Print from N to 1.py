def pri(n):
    if n == 0:
        return 
    if n == 1 :
        print(1,end="")
    else:
        print(n,end=" ")
    pri(n-1)


n = int(input())
pri(n)
