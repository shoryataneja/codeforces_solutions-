t = int(input())
for i in range(t):
    m,a,b,c, = map(int,input().split())
    # ans = 0 
    
    seated_a = min(m,a)
    seated_b = min(m,b)

    row1 = m - seated_a
    row2 = m - seated_b

    seats_left = row1 + row2 

    seated_c = min(seats_left,c)
    ans =  seated_c + seated_b + seated_a
    print(ans)