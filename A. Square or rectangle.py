t = int(input())

def helper(a,b):
    if a == b :
        return("Square")
    else:
        return("Rectangle")

for _ in range(t):
    a,b = map(int,input().split())
    print(helper(a,b))

