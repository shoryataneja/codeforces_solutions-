t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n):
        split_index = i

    lst1 = []
    lst2 = []

    for i in range(split_index):
        lst1.append(arr[i])

    for i in range(split_index,n):
        lst2.append(arr[i])