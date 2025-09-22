t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    # lst = []
    # for i in range(k):
    #     if i%n != 0:
    #         print(i)
    result = k + (k - 1) // (n - 1)
    print(result)
