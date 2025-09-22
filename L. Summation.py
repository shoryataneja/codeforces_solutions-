n = int(input())
arr = list(map(int,input().split()))

def summation(n,arr):
    if n == 1:
        return arr[0]
    return arr[n-1] + summation(n-1,arr)

print(summation(n,arr))