a,b = map(int,input().split())

if a > b:
    c = a-b 
    print(b , end =" ")
    print(c//2)

if b > a :
    c = b-a 
    print(a , end =" ")
    print(c//2)

if a == b:
    print(a,end=" ")
    print(a-b)


