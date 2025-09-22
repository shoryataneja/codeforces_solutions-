t = int(input())

for _ in range(t):
    h,m = map(int,input().split())
    ans = 0 
    hours = 24 - h 
    mins = hours*60 
    ans = mins - m 
    print(ans)