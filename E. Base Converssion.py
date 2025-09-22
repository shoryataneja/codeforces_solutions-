t = int(input())
for _ in range(t):
    n = int(input())
    def pri(n):
        if n == 1:
            return 
        lst = []
        pri(n%2)
        lst.append(n%2)
        k = lst.reverse
        return k 
    pri(n)
    print()