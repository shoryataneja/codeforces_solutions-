t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    sum_list = sum(lst)
    sqr_rut = (sum_list)**0.5
    if sqr_rut == int(sqr_rut):
        print("yes")
    else:
        print("no")