def func(arr,left,right):
    if left >=  right:
        return 
    arr[left],arr[right] = arr[right],arr[left]
    func (arr,left+1,right-1)


arr = list(map(int,input().split()))
n = len(arr)
left = 0 
right = n-1
print(func(arr,left,right))
