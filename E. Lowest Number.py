n = int(input())
arr = list(map(int,input().split()))

k = sorted(arr)

print(k[0] ,end=" ")
print(arr.index(k[0])+1)