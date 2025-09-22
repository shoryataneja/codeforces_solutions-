k,n,w = map(int,input().split())

lst = []
for i in range(1,w+1):
    lst.append(i)
lst_1 = []
for j in lst:
    lst_1.append(k*j)
t_d = sum(lst_1)
ans = (t_d-n)
print(max(0,ans))