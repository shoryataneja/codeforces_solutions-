n = int(input())
arr = list(map(int,input().split()))

max_number = arr[0]
for i in range(1,n):
    if arr[i]>max_number:
        max_number = arr[i]
    # max_number = max(arr[i],max_number) 

print(max_number)
