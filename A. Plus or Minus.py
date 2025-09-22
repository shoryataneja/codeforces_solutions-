t = int(input())
for a in range(t):
    a,b,c = map(int,input().split())

    if a + b == c :
        print("+")
    else:
        print("-")
