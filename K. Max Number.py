n = int(input())
arr = list(map(int,input().split()))

def helper(arr,n):
    if n == 1:
        return arr[0]
    
    max_arr = helper(arr,n-1)
    
    return max(arr[n-1],max_arr)

print(helper(arr,n))