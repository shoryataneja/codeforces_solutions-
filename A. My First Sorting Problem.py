t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if x < y:
        print (x, end=' ')
        print( y , ) 
    elif y < x:
        print (y, end=' ')
        print (x ) 
    else:
        print (x,end = ' ')
        print(y)

    