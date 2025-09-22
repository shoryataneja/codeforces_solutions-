t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())

    target = (a+b+c) // 3 

    if (a+b+c) % 3 == 0 and target >= a and target >= b and target <= c: 
        print("yes")
    else:
        print("no")