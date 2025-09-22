t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    i = 0
    used = False
    possible = True

    while i < n:
        if a[i] == 0:
            i += 1
        else:
            if used:
                possible = False
                break
            if i + x > n:
                i = n
            else:
                i += x
            used = True

    print("YES" if possible else "NO")
