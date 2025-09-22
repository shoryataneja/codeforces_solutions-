t = int(input())
for i in range(t):
    year = int(input())
    sqrtyear = (year)**(0.5)

    if sqrtyear != int(sqrtyear):
        print(-1)
    elif 9 >= sqrtyear >=1 :
        print(0,end=' ')
        print(int(sqrtyear))
        # print(0)
    else:
        n = sqrtyear//2 
        print(int(sqrtyear-n) , end=' ')
        print(int(n))
