n = int(input())
def pri(n):
    if n == 0 :
        return 
    pri(n-1)
    print(n)

pri(n)