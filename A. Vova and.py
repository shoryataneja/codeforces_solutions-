t = int(input())

for i in range(t):
    m , v , l , r = map(int,input().split())
    # if v == l == r :
    #     print(0)
    # else:
    #     st = abs(l-r)//v
    #     mi_st = m - st
    #     ans = (mi_st//v) -1
    #     # if mi_st % 2 != 0:
    #     #     ans -= 1 
    #     print(ans)
    blocked = (r//v) - ((l-1)//v)
    total = m//v 
    print(total-blocked)


