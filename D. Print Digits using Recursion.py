t = int(input())
for _ in range(t):
    n = int(input())
    def pri(n):
        if n == 0 :
            return
        dig = n%10
        pri(n//10)
        print(dig,end=" ")

    if n == 0:
        print(0)
        continue
    pri(n)
    print()