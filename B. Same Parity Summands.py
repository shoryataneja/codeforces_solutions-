t = int(input())  

for _ in range(t):
    n, k = map(int, input().split())
    odd_last = n - (k - 1)
    if odd_last > 0 and odd_last % 2 == 1:
        print("YES")
        print("1 " * (k - 1) + str(odd_last))
    else:
        even_last = n - 2 * (k - 1)
        if even_last > 0 and even_last % 2 == 0:
            print("YES")
            print("2 " * (k - 1) + str(even_last))
        else:
            print("NO")
