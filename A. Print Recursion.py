def pri(n):
    if n == 0:
        return 
    pri(n-1)
    print("I love Recursion")
    

n = int(input())
pri(n)